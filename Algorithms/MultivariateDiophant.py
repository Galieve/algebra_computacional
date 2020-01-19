def eea_lift(a, b, p, l, R):
    import Structures.Polynomial
    import Structures.IntegersModuleP

    IMP = Structures.IntegersModuleP.IntegersModuleP(p)
    ZPX = Structures.Polynomial.Polynomial(IMP, 'x')
    ZPXtv = ZPX.get_true_value()
    Rtv = R.get_true_value()

    amodp = ZPXtv(a.list())
    bmodp = ZPXtv(b.list())
    g, s, t = ZPX.extended_euclides(amodp, bmodp)
    assert g == ZPX.one()
    smodp = s
    tmodp = t
    modulus = p
    s = Rtv(s.list())
    t = Rtv(t.list())
    for j in range(1, l):
        e = R.sub(R.sub(R.one(), R.mul(s, a)), R.mul(t, b))
        c = ZPXtv(R.quo(e, modulus).list())
        sigma_ = ZPX.mul(smodp, c)
        tau_ = ZPX.mul(tmodp, c)
        q = ZPX.quo(sigma_, bmodp)
        sigma = ZPX.mod(sigma_, bmodp)
        tau = ZPX.add(tau_, ZPX.mul(q, amodp))

        tau = Rtv(tau.list())
        sigma = Rtv(sigma.list())
        s = R.add(s, R.mul(sigma, modulus))
        t = R.add(t, R.mul(tau, modulus))
        modulus = modulus * p

    return [s, t]




def multi_term_eealift(al, p, l, R):
    r = len(al)
    q = [R.zero()] * (r - 1)
    q[r - 2] = al[r - 1]
    for j in range(r - 3, -1, -1):
        q[j] = R.mul(q[j + 1], al[j + 1])

    beta = R.one()
    s = []
    for j in range(0, r - 1):
        sigma = multivariate_diophant([q[j], al[j]], beta, [], 0, p, l, R)
        beta = sigma[0]
        s.append(sigma[1])

    s.append(beta)
    return s


def univariate_diophant(al, x, m, p, l, R):
    import Structures.Integers
    import Structures.IntegersModuleP
    import Structures.Polynomial

    Z = Structures.Integers.Integers()
    pl = Z.repeated_squaring(p, l)

    IMP = Structures.IntegersModuleP.IntegersModuleP(pl)
    IMPX = Structures.Polynomial.Polynomial(IMP, 'x')
    IMPXtv = IMPX.get_true_value()
    Rtv = R.get_true_value()


    xm = R.repeated_squaring(x, m)
    r = len(al)

    if r > 2:
        s = multi_term_eealift(al, p, l, R)
        result = []
        for j in range(0, r):
            rem = IMPX.mod(IMPXtv(R.mul(xm, s[j]).list()), IMPXtv(al[j].list()))
            result.append(R.symmetric_module(Rtv(rem.list()), pl))
    else:
        s = eea_lift(al[1], al[0], p, l, R)
        xms0 = IMPXtv(R.mul(xm, s[0]).list())
        qxms0, mxms0 = IMPX.quo_rem(xms0, IMPXtv(al[0].list()))
        q = R.symmetric_module(Rtv(qxms0.list()), pl)
        r1 = R.symmetric_module(Rtv(mxms0.list()), pl)
        r2 = R.symmetric_module(R.add(R.mul(xm, s[1]), R.mul(q, al[1])), pl)
        result = [r1, r2]
    return result


def multivariate_diophant_assert_value(al, c, R):
    sumdeg = 0

    for i in al:
        gr = 0
        tupla = R.generate_tuple_representation(i)
        for exp, grad in tupla:
            gr = max(gr, grad[-1])

        sumdeg = sumdeg + gr
    trc = R.generate_tuple_representation(c)
    grc = 0
    for exp, grad in trc:
        grc = max(grc, grad[-1])
    return sumdeg > grc



# al = list of polynomials
# c = polynomial
# I = ideal
# d > 0, maximo grado del resultado admisible
# p = prime
# k = p**k
def multivariate_diophant(al, c, I, d, p, l, R):

    assert multivariate_diophant_assert_value(al, c, R)

    import Structures.Integers
    Z = Structures.Integers.Integers()
    pl = Z.repeated_squaring(p, l)
    # paso 1
    r = len(al)
    v = 1 + len(I)
    if v > 1:

        # paso 2.1, mv case

        A = R.prod_list(al)
        bl = [R.zero()] * r
        for j in range(0, r):
            bl[j] = R.quo(A, al[j])

        anew = []
        for i in al:
            anew.append(R.evaluate(i, I[v-2]))

        cnew = R.evaluate(c, I[v - 2])
        Inew = I[0:v - 2]

        # cuidao! (tipos)
        sigma = multivariate_diophant(anew, cnew, Inew, d, p, l, R.get_domain())
        e = R.symmetric_module(R.sub(c, R.prod_esc(sigma, bl)), pl)
        monomial = R.one()

        x = R.get_variable()

        for m in range(1, d + 1):
            if e == R.zero():
                break
            monomial = R.mul(monomial, R.sub(x, I[v - 2]))
            xjaj = R.sub(x, I[v - 2])
            pdtys = R.p_adic_taylor_series(e, xjaj)
            if len(pdtys) > m:
                cm = pdtys[m]
            else:
                cm = R.zero()
            if cm != R.zero():
                deltas = multivariate_diophant(anew, cm, Inew, d, p, l, R.get_domain())
                for i in range(0, r):
                    deltas[i] = R.mul(deltas[i], monomial)
                    sigma[i] = R.add(sigma[i], deltas[i])
                e = R.symmetric_module(R.sub(e, R.prod_esc(deltas, bl)), pl)
    else:

        # paso 2.2 uv case

        x = R.get_variable()
        sigma = [R.zero()] * r
        cl = c.list()
        for m in range(0, len(cl)):
            if cl[m] == R.get_domain().zero():
                continue
            cm = cl[m]
            deltas = univariate_diophant(al, x, m, p, l, R)
            for i in range(0, r):
                deltas[i] = R.mul(deltas[i], cm)
                sigma[i] = R.add(sigma[i], deltas[i])


    # paso 3
    sol = []
    for i in sigma:
        sol.append(R.symmetric_module(i, pl))
    return sol