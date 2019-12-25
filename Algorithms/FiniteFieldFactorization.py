from Structures.Integers import Integers


def sfd(f, R):
    assert (f.degree() > 0)
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
    assert (f.degree() > 0)
    x = R.get_variable()
    h = [x]  # h0 = x
    i = 0
    q = R.get_domain().get_order()
    fl = [f]
    g = []
    while fl[i] != R.one():
        i = i + 1
        h.append(R.mod(R.repeated_squaring(h[i - 1], q), f))
        g.append(R.gcd(R.sub(h[i], x), fl[i - 1]))
        fl.append(R.quo(fl[i - 1], g[i - 1]))
    return g


def equal_degree_splitting(f, d, R):
    n = f.degree()
    a = R.random_element(n)
    q = R.get_domain().get_order()
    if len(a.list()) < 2:
        return None
    g1 = R.gcd(a, f)
    if g1 != R.one():
        return g1
    qd = (Integers().repeated_squaring(q, d) - 1) // 2
    b = R.mod(R.repeated_squaring(a, qd), f)
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
