from Algorithms.MultivariateDiophant import multivariate_diophant


def subsitute(j, pl, A, I, S):
    T = S.get_domain()
    A[j - 1] = T.symmetric_module(S.evaluate(A[j], I[j - 1]), pl)
    S = T
    return A, S

# IT HAS BUGS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# I = [c2...cn] => I = <x2-c2..., xn-cn>
def multivariate_hensel_lifting(a, R, I, p, l, ul, lcul):

    import Structures.Integers
    import Structures.IntegersModuleP
    import Structures.Polynomial
    Z = Structures.Integers.Integers()
    pl = Z.repeated_squaring(p, l)
    IMP = Structures.IntegersModuleP.IntegersModuleP(pl)
    IMPX = Structures.Polynomial.Polynomial(IMP, 'x0')

    # paso 1
    v = 1 + len(I)
    A = [R.zero()] * v
    A[v - 1] = R.symmetric_module(a, pl)
    domain_list = [R] * v
    domain_list_pl = [IMPX] * v
    for i in range(1, v):
        IMPX = Structures.Polynomial.Polynomial(IMPX, 'x' + str(i))
        domain_list_pl[i] = IMPX


    domain_list[v - 1] = R
    x_list = [R.get_variable()] * v
    x_list[v - 1] = R.get_variable()
    for j in range(v - 1, 0, -1):
        A, S = subsitute(j, pl, A, I, domain_list[j])
        domain_list[j - 1] = S
        x_list[j - 1] = S.get_variable()
    # en A[0] tenemos un polinomio en Z[x] = S

    tra = R.generate_tuple_representation(a)
    maxdeg = 0
    for c, l_ in tra:
        for i in range(0, len(l_) - 1):
            maxdeg = max(maxdeg, l_[i])

    U = list(ul)
    n = len(ul)

    # paso 2
    for j in range(1, v):

        # paso 2.1
        U1 = U;
        monomial = domain_list_pl[j].one()
        dlpltv =  domain_list_pl[j].get_true_value()
        uaux = []
        for i in U:
            uaux.append(dlpltv(i.list()))
        U = uaux
        for m in range(0, n):

            if lcul[m] != 1:
                S = domain_list_pl
                aux = [lcul[m]] * v
                aux[v - 1] = lcul[m]
                # CUIDAO: INDICES DE I
                for k in range(v - 1, j - 1, -1):
                    aux, S = subsitute(k, pl, aux, I, S)
                tpru = domain_list_pl[j].generate_tuple_representation(dlpltv(U[m].list()))
                # cuidado con los ceros!
                c, l_ = tpru[-1]
                tpru[-1] = (aux[j - 1] , l_)
                U[m] = domain_list_pl[j].generate_polynomial(tpru)
        prod = domain_list_pl[j].prod_list(U)
        e = domain_list_pl[j].sub(dlpltv(A[j].list()), prod)

        # paso 2.2
        for k in range(1, domain_list[j].degree(A[j]) + 1):
            if e == R.zero():
                break
            monomial = domain_list_pl[j].mul(monomial, dlpltv(domain_list[j].sub(x_list[j], I[j - 1]).list()))
            xjaj = domain_list[j].sub(x_list[j], I[j - 1])
            monomial = dlpltv(monomial.list()); xjaj = dlpltv(xjaj.list())
            IMPX = domain_list_pl[j]
            pdtys = IMPX.p_adic_taylor_series(IMPX.get_true_value()(e.list()),IMPX.get_true_value()(xjaj.list()))
            if len(pdtys) > k:
                c = domain_list[j].get_true_value()(pdtys[k])
            else:
                c = domain_list[j].zero()
            if c != domain_list[j].zero():
                deltau = multivariate_diophant(U1, c, I[0: j - 1], maxdeg, p, l, domain_list[j])
                for i in range(0, len(deltau)):
                    deltau[i] = R.mul(deltau[i], monomial)
                    U[i] = domain_list[j].symmetric_module(domain_list[j].add(U[i], deltau[i]), pl)
                e = domain_list[j].sub(A[j],  domain_list[j].prod_list(U))

    # paso 3
    if a == R.prod_list(U):
        return U
    else:
        return None