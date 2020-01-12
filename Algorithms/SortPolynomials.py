def lexicografic_mon((a, la), (b, lb)):
    n = len(la)
    assert n == len(lb)
    for i in range(0, n):
        if la[i] < lb[i]:
            return -1
        elif la[i] > lb[i]:
            return 1
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


def rev_lexicografic_mon((a, la), (b, lb)):
    n = len(la)
    assert n == len(lb)
    for i in range(n - 1, -1, -1):
        if la[i] < lb[i]:
            return -1
        elif la[i] > lb[i]:
            return 1
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


def graded_lexicografic_mon((a, la), (b, lb)):
    n = 0
    for i in la:
        n = n + i
    m = 0
    for i in lb:
        m = m + i
    if n < m:
        return -1
    elif n > m:
        return 1
    else:
        return lexicografic_mon((a, la), (b, lb))


def sort_polynomials(lf, lg, order):
    lf.sort(cmp=order, reverse=True)
    lg.sort(cmp=order, reverse=True)
    n = min(len(lf), len(lg))
    for i in range(0, n):
        c = order(lf[i], lg[i])
        if c != 0:
            return c

    if len(lf) == len(lg):
        return 0
    elif len(lf) < len(lg):
        return -1
    else:
        return 1
