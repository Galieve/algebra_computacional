# Algorithms for computer algebra, Geddes et al


# a, b in R, R es D.E.
# return gcd(a, b)
def euclides(a, b, R):
    c = R.normal(a)
    d = R.normal(b)
    while not d == R.zero():
        r = R.mod(c, d)
        c = d
        d = r
    return R.normal(c)

# a, b in R
# return gcd(a,b), s, t tal que a * s + b * t = gcd(a, b)
def extended_euclides(a, b, R):
    c = R.normal(a);
    d = R.normal(b)
    c1 = R.one();
    d1 = R.zero();
    c2 = R.zero();
    d2 = R.one();
    while not d == R.zero():
        q = R.quo(c, d);
        r = R.sub(c, R.mul(q, d));
        r1 = R.sub(c1, R.mul(q, d1));
        r2 = R.sub(c2, R.mul(q, d2));
        c = d;
        c1 = d1;
        c2 = d2;
        d = r;
        d1 = r1;
        d2 = r2;
    g = R.normal(c)
    s = R.quo(c1, R.mul(R.unit_normal(a), R.unit_normal(c)))
    t = R.quo(c2, R.mul(R.unit_normal(b), R.unit_normal(c)))

    return g, s, t
