def new_prime(a, b, R):
    import Structures.Integers
    import Structures.IntegersModuleP
    a_ = R.lc(a)
    b_ = R.lc(b)
    Z = Structures.Integers.Integers()
    p = abs(Z.get_random()) + 2
    IMP = Structures.IntegersModuleP.IntegersModuleP(p)
    valid = IMP.canonical(a_) != IMP.zero() and IMP.canonical(b_) != IMP.zero()
    while not Z.aks(p) or not valid:
        p = abs(Z.get_random()) + 2
        IMP = Structures.IntegersModuleP.IntegersModuleP(p)
        valid = IMP.canonical(a_) != IMP.zero() and IMP.canonical(b_) != IMP.zero()
    return p


def new_evaluation_point(a, b, R):
    import numpy as np
    lcoa = R.lc(a)
    lcob = R.lc(b)
    n = R.number_of_variables()

    vbec = [R.zero()] * n
    valid = R.evaluatemv(lcoa, vbec) != R.zero() and R.evaluate(lcob, vbec) != R.zero()
    while not valid:
        p = np.random.poisson(1, 1)[0]
        if p > n:
            p = p % n

        vbec = [R.zero()] * n
        for i in range(0, p):
            vbec[i] = R.get_domain().random_element()

        import random
        random.shuffle(vbec)
        valid = R.evaluatemv(lcoa, vbec) != R.zero() and R.evaluate(lcob, vbec) != R.zero()
        
    return vbec


    return None









def ez_gcd(a, b, R):

    # paso 1
    S = R.get_domain()
    conta =  R.cont(a)
    contb = R.cont(b)
    a = R.primitive_part(a)
    b = R.primitive_part(b)
    g = S.gcd(conta, contb)
    conta = S.quo(conta, g)
    contb = S.quo(contb, g)

    # paso 2
    p = new_prime(a, b, R)

    # paso 3
    bvec = new_evaluation_point(a, b, R)


