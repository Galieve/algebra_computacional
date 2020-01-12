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
