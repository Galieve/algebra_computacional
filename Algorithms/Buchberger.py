def s_polynomial(g, h, R):
    ltg = R.lt(g)
    lth = R.lt(h)
    mdegg = R.multidegree(g)
    mdegh = R.multidegree(h)
    gamma = []
    assert len(mdegg) == len(mdegh)
    n = len(mdegg)
    for i in range(0, n):
        gamma.append(max(mdegg[i], mdegh[i]))
    xgamma = R.generate_monomial((R.get_bottom_domain().one(), gamma))
    s = R.quo(R.mul(xgamma, g), ltg)
    s = R.sub(s, R.quo(R.mul(xgamma, h), lth))
    return s


def buchberger_algorithm(lfi, R):
    # paso 1
    G = lfi

    # paso 2
    while True:

        # paso 3
        S = []
        G = R.sort_polynomials(G, True)
        t = len(G)
        for i in range(0, t):
            for j in range(i + 1, t):

                # paso 4
                spol_ij = s_polynomial(G[i], G[j], R)
                lq, r = R.multivariate_division(spol_ij, G)

                if r != R.zero():
                    S.append(r)

        # paso 5
        if len(S) == 0:
            return G
        else:
            G.extend(S)
            G = list(set(G))

def ideal_membership_testing(f, base, R):
    q, r = R.multivariate_division(f, base)
    return r == R.zero()


def minimal_buchberger_algorithm(lfi, R):

    # paso 1
    base = buchberger_algorithm(lfi, R)

    # paso 2
    sol = list(base)
    for i in range(0, len(base)):

        g = base[i]
        ltg = R.lt(g)
        bc = list(sol)
        bc.remove(g)

        # paso 3
        lgbase = []
        for i in bc:
            lgbase.append(R.lt(i))
        lgbase = buchberger_algorithm(lgbase, R)

        # paso 4
        if ideal_membership_testing(ltg, lgbase, R):
            sol = bc

    # paso 5
    sol_ = []
    for i in sol:
        sol_.append(R.mul(R.get_bottom_domain().inverse(R.lc(i)), i))

    # paso 6
    return sol_

def minimal_reduced_buchberger_algorithm(lfi, R):

    # paso 1
    mba = minimal_buchberger_algorithm(lfi, R)

    # paso 2
    answ = []
    n = len(mba)
    for i in range(0, n):
        ideal_base = answ[0:i]
        ideal_base.extend(mba[i+1:n])

        # paso 3
        q, r = R.multivariate_division(mba[i], ideal_base)
        answ.append(r)

    # paso 4
    return answ


