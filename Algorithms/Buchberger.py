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
    xgamma = R.generate_monomial((1, gamma))
    s = R.quo(R.mul(xgamma, g), ltg)
    s = R.sub(s, R.quo(R.mul(xgamma, h), lth))
    return s


def buchberger_algorithm(lfi, R):
    G = lfi
    while True:
        S = []
        G = R.sort_polynomials(G, True)
        t = len(G)
        for i in range(0, t):
            for j in range(i + 1, t):
                spol_ij = s_polynomial(G[i], G[j], R)
                lq, r = R.multivariate_division(spol_ij, G)
                if r != R.zero():
                    S.append(r)

        if len(S) == 0:
            return G
        else:
            G.extend(S)
            G = list(set(G))

def ideal_membership_testing(f, base, R):
    q, r = R.multivariate_division(f, base)
    return r == R.zero()


def minimal_buchberger_algorithm(lfi, R):
    base = buchberger_algorithm(lfi, R)


    sol = list(base)
    for i in range(0, len(base)):
        g = base[i]
        ltg = R.lt(g)
        bc = list(sol)
        bc.remove(g)
        lgbase = []
        for i in bc:
            lgbase.append(R.lt(i))
        lgbase = buchberger_algorithm(lgbase, R)
        if ideal_membership_testing(ltg, lgbase, R):
            sol = bc
    sol_ = []
    for i in sol:
        sol_.append(R.mul(R.get_bottom_domain().inverse(R.lc(i)), i))
    return sol_

def minimal_reduced_buchberger_algorithm(lfi, R):
    mba = minimal_buchberger_algorithm(lfi, R)
    answ = []
    n = len(mba)
    for i in range(0, n):
        ideal_base = answ[0:i]
        ideal_base.extend(mba[i+1:n])
        q, r = R.multivariate_division(mba[i], ideal_base)
        answ.append(r)
    return answ


