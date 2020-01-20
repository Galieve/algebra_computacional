# A computational introduction to number theory and algebra


def get_th(n):
    t = n
    h = 0
    while t % 2 == 0:
        h = h + 1
        t = t // 2
    return t, h


# ln = {a in Zn+, a**(t*2**h) == 1 and a**(t*2**(j+1)) == 1 => a**(t*2**j) == +-1}
def check_ln(a, IMP, t, h):
    b = IMP.repeated_squaring(a, t)
    if b == IMP.one():
        return True
    for j in range(0, h):
        if b == IMP.get_order() - 1:
            return True
        elif b == IMP.one():
            return False
        b = IMP.mul(b, b)
    return False


def miller_rabin(n, k):
    assert n > 1
    import Structures.IntegersModuleP
    IMP = Structures.IntegersModuleP.IntegersModuleP(n)

    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    t, h = get_th(n - 1)

    for i in range(0, k):
        a = IMP.get_random(2, n - 1)
        if not check_ln(a, IMP, t, h):
            return False
    return True
