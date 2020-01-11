
def sfd(f, R):
    assert (R.degree(f) > 0)
    l = []
    s = 1
    while f != R.one():
        j = 1
        g = R.quo(f, R.gcd(f, R.derivate(f)))
        while g != R.one():
            f = R.quo(f, g)
            h = R.gcd(f, g)
            m = R.quo(g, h)
            if m != R.one():
                l.append((m, j * s))
            g = h
            j = j + 1
        if f != R.one():
            p = R.get_domain().get_char()
            f = R.pth_root(f, p)
            s = p * s
    return l


def distinct_degree_decomposition(f, R):
    assert (R.degree(f) > 0)
    x = R.get_variable()
    h = [x]  # h0 = x
    i = 0
    q = R.get_domain().get_order()
    fl = [f]
    g = []
    import Structures.QuotientFiniteField
    QF = Structures.QuotientFiniteField.QuotientFiniteField(R, f)
    while fl[i] != R.one():
        i = i + 1
        h.append(QF.repeated_squaring(h[i - 1], q))
        g.append(R.gcd(R.sub(h[i], x), fl[i - 1]))
        fl.append(R.quo(fl[i - 1], g[i - 1]))
    return g


def equal_degree_splitting(f, d, R):
    n = R.degree(f)
    a = R.random_element(n)
    if len(a.list()) < 2:
        return None
    q = R.get_domain().get_order()
    assert(q %2 == 1)
    g1 = R.gcd(a, f)
    if g1 != R.one():
        return g1
    import Structures.Integers
    import Structures.QuotientFiniteField
    qd = (Structures.Integers.Integers().repeated_squaring(q, d) - 1) // 2
    b = Structures.QuotientFiniteField.QuotientFiniteField(R, f).repeated_squaring(a, qd)
    g2 = R.gcd(R.sub(b, R.one()), f)
    if g2 != R.one() and g2 != f:
        return g2
    else:
        return None


def equal_degree_splitting_ktimes(f, d, R, k):
    for i in range(0, k):
        g = equal_degree_splitting(f, d, R)
        if g is not None:
            return g
    # low probability
    return None


def equal_degree_full_splitting(f, d, R, k):
    n = R.degree(f)
    if n == d:
        return [f]
    g = equal_degree_splitting_ktimes(f, d, R, k)
    if g is None:
        return None
    l1 = equal_degree_full_splitting(g, d, R, k)
    l2 = equal_degree_full_splitting(R.quo(f, g), d, R, k)
    if l1 is not None and l2 is not None:
        l1.extend(l2)
    elif l2 is not None:
        l1 = l2
    return l1