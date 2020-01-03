

def euclides(a, b, R):
    c = R.normal(a)
    d = R.normal(b)
    while not d == R.zero():
        r = R.mod(c, d)
        c = d
        d = r
    return R.normal(c)


# given a*s+b*t=mcd(a,b) return (g = mcd(a,b), s, t)
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
