from math import ceil, sqrt


def to_binary(n):
    assert (n >= 0)
    if n == 0:
        return [0]

    l = []
    while n != 0:
        l.append(n % 2)
        n = n // 2
    return l


def eratostenes(n):
    m = sqrt(n)
    l = [True] * int(ceil(m)+2)
    l[0] = False
    l[1] = False
    lp = []
    for i in range(2, len(l)):
        if l[i]:
            lp.append(i)
            for j in range(i * i, len(l), i):
                l[j] = False
    return lp


def factorlp(n, lp):
    assert (n > 1)
    vp = []
    i = 0
    while i < len(lp):
        if n == 1:
            return vp
        # s(n) >= todos los factores primos que quedan.
        # n no se puede expresar como n = a * b, a >= b, a,b != 1, ya que el mayor menor es sqrt(n) y no factoriza
        elif int(ceil(sqrt(n))) < lp[i]:
            vp.append(n)
            return vp
        elif n % lp[i] == 0:
            vp.append(lp[i])
            n = n // lp[i]
        else:
            i = i + 1
    if n != 1:
        vp.append(n)
    return vp


def factor(n):
    lp = eratostenes(n)
    return factorlp(n, lp)
