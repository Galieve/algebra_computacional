from math import ceil, log, floor, sqrt

from Algorithms.MathAuxiliar import to_binary


def is_power(n):
    k = int(ceil(log(n, 2)))
    for b in range(2, k + 1):
        a = n**(1./b)
        if floor(a) == a:
            return True
    return False

def find_r(n, R):

    import Structures.IntegersModuleP
    for r in range(2, n + 1):
        IMP = Structures.IntegersModuleP.IntegersModuleP(r)
        if R.gcd(n, r) > 1 \
                or (R.gcd(n, r) == 1
                    and IMP.multiplicative_order(n) > 4 * (len(to_binary(n))**2)):
            return r
    # n it's always an answer
    return n

def AKS(n):
    if is_power(n):
        return False
    import Structures.Integers
    R = Structures.Integers.Integers()
    r = find_r(n, R)
    if r == n:
        return True
    elif R.gcd(n, r) > 1:
        return False
    k = len(to_binary(n))
    rs = int(floor(sqrt(r)))
    import Structures.IntegersModuleP
    import Structures.Polynomial
    IMP = Structures.IntegersModuleP.IntegersModuleP(n)
    R = Structures.Polynomial.Polynomial(IMP, 'x')
    x = R.get_variable()
    modP = x**r - 1
    for j in range (1, 2*k*rs + 1 + 1):
        lp = R.mod(R.repeated_squaring(R.add(x,j),n), modP)
        rp = R.mod(R.add(R.repeated_squaring(x,n),j), modP)
        if lp != rp:
            return False
    return True

