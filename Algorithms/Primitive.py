def primitive_euclidean(a, b, R):
    c = R.primitive_part(a)
    d = R.primitive_part(b)
    while d != R.zero():
        r = primitive_reminder(c, d)
        c = d
        d = R.primitive_part(r)
    gamma = R.get_domain().gcd(R.cont(a), R.cont(b))
    g = gamma * c
    return g


def primitive_reminder(a, b):
    if len(b.list()) == 0: return a
    beta = b.leading_coefficient()  # caution
    n = a.degree() - b.degree() + 1
    _, r = (beta ** n * a).quo_rem(b)
    return r
