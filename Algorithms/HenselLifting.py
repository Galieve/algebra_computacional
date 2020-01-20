# Modern Computer Algebra
# f is square_free
# f es primitivo si f /cont(f) == f <=> cont(f) == 1
# gcd(a_i) = cont(f)
# 2 * x + 3 = f, cont(f) = 1, p != 2
from math import sqrt, ceil, log

from Algorithms.AKS import AKS
from Algorithms.MathAuxiliar import factor

import itertools


def squarefree_charzero(f, R):
    f_ = R.derivate(f)
    u = R.gcd(f, f_)
    return R.quo(f, u)


def findsubsets(S, m):
    return list(map(set, itertools.combinations(S, m)))


def find_prime(l, sup):
    import Structures.Integers
    Z = Structures.Integers.Integers()
    p = Z.get_random(2, sup)
    while p in l or not AKS(p):
        p = Z.get_random(2, sup)
    return p


# R = Z[x], f elevado de Zpl[x] a Z[x]
def minimize_max_norm(f, R, pl):
    return R.symmetric_module(f, pl)


def minimize_max_norm_list(l, R, pl):
    res = []
    for i in l:
        res.append(minimize_max_norm(i, R, pl))
    return res


# R = Z[x]
def hensel_step(m, f, g, h, s, t, R):
    n = R.degree(f)
    import Structures.Polynomial
    import Structures.IntegersModuleP
    IMP = Structures.IntegersModuleP.IntegersModuleP(m)
    RM = Structures.Polynomial.Polynomial(IMP, 'x')
    RMtv = RM.get_true_value()

    assert f != R.zero()
    assert n == R.degree(g) + R.degree(h)
    assert R.degree(s) < R.degree(h)
    assert R.degree(t) < R.degree(g)
    assert RMtv(f.list()) == RMtv(R.mul(g, h).list())
    assert RM.one() == RMtv(R.add(R.mul(s, g), R.mul(t, h)).list())
    assert h.list()[-1] == R.get_domain().one()

    # convertimos los polinomios de Fp[x] a Fp**2[x]
    F = Structures.IntegersModuleP.IntegersModuleP(m ** 2)
    RP = Structures.Polynomial.Polynomial(F, 'x')
    RPtv = RP.get_true_value()
    f = RPtv(f.list())
    g = RPtv(g.list())
    h = RPtv(h.list())
    t = RPtv(t.list())
    s = RPtv(s.list())

    # paso 1
    e = RP.sub(f, RP.mul(g, h))
    q, r = RP.quo_rem(RP.mul(s, e), h)
    g_ = RP.add(g, RP.add(RP.mul(t, e), RP.mul(q, g)))
    h_ = RP.add(h, r)

    # paso 2
    b = RP.add(RP.mul(s, g_), RP.sub(R.mul(t, h_), RP.one()))
    c, d = RP.quo_rem(RP.mul(s, b), h_)
    s_ = RP.sub(s, d)
    t_ = RP.sub(t, R.add(R.mul(t, b), R.mul(c, g_)))

    # paso 3
    Rtv = R.get_true_value()
    g_ = Rtv(g_.list())
    h_ = Rtv(h_.list())
    s_ = Rtv(s_.list())
    t_ = Rtv(t_.list())

    return g_, h_, s_, t_


def multifactor_hensel_lifting(p, lc, hlist, RP, f, R, l):
    import Structures.Polynomial
    import Structures.IntegersModuleP
    import Structures.Integers
    Z = Structures.Integers.Integers()

    Rtv = R.get_true_value()
    # paso 1
    r = len(hlist)
    if r == 1:
        pl = Z.repeated_squaring(p, l)
        IMP = Structures.IntegersModuleP.IntegersModuleP(pl)
        lc_inverse = IMP.inverse(lc)
        RK = Structures.Polynomial.Polynomial(IMP, 'x')
        f = RK.get_true_value()(f.list())
        res = RK.mul(lc_inverse, f)
        return [Rtv(res)]

    # paso 2
    k = r // 2
    d = int(ceil(log(l, 2)))

    # paso 3
    f_ = R.get_true_value()(f.list())
    g = [lc]
    for i in range(0, k):
        g[0] = RP.mul(g[0], hlist[i])

    h = [RP.one()]
    for i in range(k, r):
        h[0] = RP.mul(h[0], hlist[i])

    # paso 4
    s = []
    t = []
    if AKS(p):
        gcd, s_, t_ = RP.extended_euclides(g[0], h[0])
        assert gcd == R.one()
        s.append(s_)
        t.append(t_)
    else:
        assert False

    # los convertimos de nuevo en polinomios de Z[x]
    g[0] = Rtv(g[0].list())
    h[0] = Rtv(h[0].list())
    s[0] = Rtv(s[0].list())
    t[0] = Rtv(t[0].list())

    # paso 5
    for j in range(1, d + 1):
        # paso 6
        m = Z.repeated_squaring(p, Z.repeated_squaring(2, j - 1))
        g_, h_, s_, t_ = hensel_step(m, f_, g[j - 1], h[j - 1], s[j - 1], t[j - 1], R)
        g.append(g_)
        h.append(h_)
        s.append(s_)
        t.append(t_)

    # paso 7
    g = g[d]
    h = h[d]

    # paso 8
    res = multifactor_hensel_lifting(p, g.list()[- 1], hlist[0: k], RP, g, R, l)

    # paso 9
    res_ = multifactor_hensel_lifting(p, h.list()[- 1], hlist[k: r], RP, h, R, l)

    # paso 10
    res.extend(res_)
    return res


def hensel_lifting(f, R):
    import Structures.FiniteFieldsWrapper
    import Structures.FiniteFieldPolynomial
    import Structures.Integers
    import Structures.IntegersModuleP
    import Structures.Polynomial

    # paso 1
    n = R.degree(f)
    F = R.get_domain()
    Z = Structures.Integers.Integers()

    if n == 1:
        return [f]
    b = f.list()[-1]

    if b > 1:
        list_lc = set(factor(b))
    elif b < - 1:
        list_lc = set(factor(-b))
    else:
        list_lc = []


    A = R.max_norm(f)
    B = sqrt(n + 1) * Z.repeated_squaring(2, n) * A * b
    C = Z.repeated_squaring(n + 1, 2 * n) * Z.repeated_squaring(A, 2 * n - 1)
    gamma = int(ceil(2 * log(C, 2)))

    # paso 2
    limsup = int(ceil(2 * gamma * log(gamma)))
    p = find_prime(list_lc, limsup)
    FP = Structures.FiniteFieldsWrapper.FiniteFieldsWrapper(p, 1, 'a')
    RP = Structures.FiniteFieldPolynomial.FiniteFieldPolynomial(FP, 'x')
    fmod = RP.get_true_value()(f.list())
    fder = RP.derivate(fmod)

    while RP.gcd(fmod, fder) != RP.one() or p == 2:
        p = find_prime(list_lc, limsup)
        FP = Structures.FiniteFieldsWrapper.FiniteFieldsWrapper(p, 1, 'a')
        RP = Structures.FiniteFieldPolynomial.FiniteFieldPolynomial(FP, 'x')
        fmod = RP.get_true_value()(f.list())
        fder = RP.derivate(fmod)

    logB = log(2 * B + 1.0, p)
    l = int(ceil(logB))

    # paso 3
    f_ = RP.quo(RP.get_true_value()(f.list()), b)
    hlist = RP.berlekamp(f_, FP.get_order())
    hlist = minimize_max_norm_list(hlist, R, p)

    # paso 4
    pl = Z.repeated_squaring(p, l)
    flist = multifactor_hensel_lifting(p, b, hlist, RP, f, R, l)
    flist = minimize_max_norm_list(flist, R, pl)
    r = len(flist)

    # paso 5
    T = set([i for i in range(0, r)])
    s = 1
    G = []
    f_ = f

    # paso 6
    FL = Structures.IntegersModuleP.IntegersModuleP(pl)
    RL = Structures.Polynomial.Polynomial(FL, 'x')
    RLtv = RL.get_true_value()

    while 2 * s <= len(T):
        break_bool = False

        # paso 7
        subsets = findsubsets(T, s)
        for S in subsets:
            # paso 8
            S = set(S)
            h_ = g_ = RLtv(b)
            for i in S:
                g_ = RL.mul(g_, RLtv(flist[i].list()))

            for i in T:
                if i in S:
                    continue
                h_ = RL.mul(h_, RLtv(flist[i].list()))

            # paso 9

            g_ = R.get_true_value()(g_.list())
            h_ = R.get_true_value()(h_.list())
            g_ = minimize_max_norm(g_, R, pl)
            h_ = minimize_max_norm(h_, R, pl)

            if F.mul(R.one_norm(g_), R.one_norm(h_)) <= B:
                for i in S:
                    T.discard(i)
                G.append(R.primitive_part(g_))
                f_ = R.primitive_part(h_)
                if f_ != R.zero():
                    b = f_.list()[-1]
                break_bool = True
                break

        # paso 10
        if not break_bool:
            s = s + 1
            T_complement = []

    # paso 11
    G.append(f_)
    return G


def hensel_full_lifting(f, R):

    if f == R.zero():
        return [f]
    l = []
    if R.normal(f) != f:
        l.append(-1)

    b = R.cont(f)
    f = R.primitive_part(f)

    if b > 1:
        l.extend(factor(b))

    l.extend(hensel_lifting(R.primitive_part(f), R))
    return l
