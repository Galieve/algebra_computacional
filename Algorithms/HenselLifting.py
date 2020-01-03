
# f is square_free
# f es primitivo si f /cont(f) == f <=> cont(f) == 1
# gcd(a_i) = cont(f)
# 2 * x + 3 = f, cont(f) = 1, p != 2
from math import sqrt, ceil, log2

from Algorithms.AKS import AKS
from Algorithms.MathAuxiliar import factor

def find_prime(l, sup):
    import Structures.Integers
    Z = Structures.Integers.Integers()
    p = Z.get_random(sup)
    while p in l or not AKS(p):
        p = Z.get_random(sup)
    return p

def max_norm(f, R):
    fl = f.list()
    if len(fl) == 0:
        return 0
    maxn = abs(f[0])
    for i in fl:
        maxn = max(abs(i), maxn)
    return maxn


# p = 2, l = 2, f = 3 * x + 1 // g = 2 * x + 1

# f === 1 * (x + 1) (mod p, 2) -> x + 1
# f === 3 * (x + 3) (mod p **l, 4) -> x + 3
def multifactor_hensel_lifting(p, lc, F, hlist, f, R, l):
    import Structures.FiniteFields
    import Structures.Polynomial
    import Structures.IntegersModuleP
    import Structures.Integers
    Z = Structures.Integers.Integers()

    # paso 1
    r = len(hlist)
    if r == 1:
        pl = Z.repeated_squaring(p, l)
        IMP = Structures.IntegersModuleP.IntegersModuleP(pl)
        lc_inverse = IMP.inverse(lc)
        K = Structures.FiniteFields.FiniteFields(p, l, 'a')
        RK = Structures.Polynomial.Polynomial(K, 'x')
        f = RK.get_true_value(f.list())
        return RK.mul(lc_inverse, f)

    # paso 2
    k = r // 2
    d = int(ceil(log2(l)))

    # paso 3





def hensel_lifting(f, R):

    import Structures.FiniteFields
    import Structures.Polynomial
    import Structures.Integers

    # paso 1
    n = R.degree(f)
    Z = Structures.Integers.Integers()
    if n == 1:
        return f
    b = f.list()[-1]
    list_lc = set(factor(b))
    A = max_norm(f, R)
    B = sqrt(n + 1) *  Z.repeated_squaring(2, n) * A * b
    C = Z.repeated_squaring(n + 1, 2*n) * Z.repeated_squaring(A, 2*n - 1)
    gamma = int(ceil(2 * log2(C)))

    # paso 2
    p = find_prime(list_lc)
    FP = Structures.FiniteFields.FiniteFields(p, '1', 'a')
    RP = Structures.Polynomial.Polynomial(FP, 'x')
    fmod = RP.get_true_value()(f.list())
    fder = RP.derivate(fmod)
    while RP.gcd(fmod, fder) != RP.one():
        p = find_prime(list_lc)
        FP = Structures.FiniteFields.FiniteFields(p, '1', 'a')
        RP = Structures.Polynomial.Polynomial(FP, 'x')
        fmod = RP.get_true_value()(f.list())
        fder = RP.derivate(fmod)

    # paso 3

    hlist = RP.berlekamp(f, FP.get_order())

    # paso 4
