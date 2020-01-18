from Algorithms.MultivariateDiophant import multivariate_diophant


def subsitute(j, pl, A, I, S):
    T = S.get_domain()
    A[j - 1] = T.symmetric_module(S.evaluate(A[j], I[j - 1]), pl)
    S = T
    return A, S

# I = [c2...cn] => I = <x2-c2..., xn-cn>
def multivariate_hensel_lifting(a, R, I, p, l, ul, lcul):

    import Structures.Integers
    Z = Structures.Integers.Integers()
    pl = Z.repeated_squaring(p, l)

    # paso 1
    v = 1 + len(I)
    A = [] * v
    A[v - 1] = R.symmetric_module(a)
    domain_list = [] * v
    domain_list[v - 1] = R
    x_list = [] * v
    x_list[v - 1] = R.get_variable()
    for j in range(v - 1, 0, -1):
        A, S = subsitute(j, pl, A, I, domain_list[j])
        domain_list[j - 1] = S
        x_list[j - 1] = S.get_variable()
    # en A[0] tenemos un polinomio en Z[x] = S

    tra = R.generate_tuple_representation(a)
    maxdeg = 0
    for c, l in tra:
        for i in range(1, len(l)):
            maxdeg = max(maxdeg, i)

    U = ul
    n = len(ul)

    # paso 2
    for j in range(1, v + 1):

        # paso 2.1
        U1 = U; monomial = R.one()
        for m in range(1, n + 1):
            if lcul[m] != 1:
                S = R
                aux = [] * v
                aux[v - 1] = lcul[m]
                # CUIDAO: INDICES DE I
                for k in range(v - 1, j - 1, -1):
                    aux, S = subsitute(k, pl, aux, I, S)
                tpru = R.generate_tuple_representation(U[m])
                # cuidado con los ceros!
                c, l = tpru[-1]
                tpru[-1] = (aux[j - 1] , l)
                U[m] = R.generate_polynomial(tpru)

        prod = R.prod_list(U)
        e = A[j] - prod

        # paso 2.2
        for k in range(1, domain_list[j].degree(A[j])):
            while e != R.zero():
                monomial = R.mul(monomial, R.sub(x_list[j], I[j]))
                xjaj = R.sub(x_list[j], I[j])
                pdtys = R.p_adic_taylor_series(e, xjaj)
                if len(pdtys) > k:
                    c = pdtys[k]
                else:
                    c = R.zero()
                if c != R.zero():
                    deltau = multivariate_diophant(U1, c, I[0: j - 1], maxdeg, p, l, R)
                    deltau = R.mul(deltau, monomial)
                    u = R.symmetric_module(R.add(u, deltau), pl)
                    e = R.sub(A[j],  R.prod_list(U))

    # paso 3
    if a == R.prod_list(U):
        return U
    else:
        return None