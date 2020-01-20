# Wikipedia


# alpha, beta in IMP, x in R.
# choose a "random" set for x and multiply x.
# S3 == 0, S1 == 2, S2 == 1
def new_xab(alpha, beta, x, a, b, R, IMP):
    import Structures.QuotientFiniteField
    if issubclass(type(R), Structures.QuotientFiniteField.QuotientFiniteField):
        tpr = R.get_domain().generate_tuple_representation(x)
        x0, _ = tpr[0]
        x0 = x0.integer_representation()
    else:
        xl = x.list()
        x0 = xl[0].lift()
    if x0 % 3 == 0:
        return R.mul(x, x), IMP.mul(2, a), IMP.mul(2, b)
    elif x0 % 3 == 1:
        return R.mul(beta, x), a, IMP.add(b, IMP.one())
    else:
        return R.mul(alpha, x), IMP.add(a, IMP.one()), b


# beta, alpha in R, R == field, n order of <beta>
# return x tal que beta**x = alpha or None (fail)
def discrete_logarithm_n(alpha, beta, R, n):
    import Structures.IntegersModuleP
    IMP = Structures.IntegersModuleP.IntegersModuleP(n)
    import Structures.Integers
    Z = Structures.Integers.Integers()
    x = R.one()
    a = IMP.zero()
    b = IMP.zero()
    x_ = R.one()
    a_ = IMP.zero()
    b_ = IMP.zero()
    for i in range(1, n + 1):
        x, a, b = new_xab(alpha, beta, x, a, b, R, IMP)
        x_, a_, b_ = new_xab(alpha, beta, x_, a_, b_, R, IMP)
        x_, a_, b_ = new_xab(alpha, beta, x_, a_, b_, R, IMP)
        if x == x_:
            r = IMP.sub(b_, b)
            s = IMP.sub(a, a_)
            if Z.gcd(s, n) != Z.one():
                return None
            else:
                return IMP.mul(IMP.inverse(s), r)
    # no deberia entrar por aqui
    return None


# output => beta**out = alpha
def discrete_logarithm(alpha, beta, R):
    return discrete_logarithm_n(alpha, beta, R, R.multiplicative_order(beta))
