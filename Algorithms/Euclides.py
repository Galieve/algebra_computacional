

def euclides(a, b, n, mod, zero):
    c = n(a)
    d = n(b)
    while not d == zero():
        r = mod(c, d)
        c = d
        d = r
    return n(c)


# given a*s+b*t=mcd(a,b) return (g = mcd(a,b), s, t)
def extended_euclides(a, b, n, u, div, mul, sub, zero, one):
    c = n(a);
    d = n(b)
    c1 = one();
    d1 = zero();
    c2 = zero();
    d2 = one();
    while not d == zero():
        q = div(c, d);
        r = sub(c, mul(q, d));
        r1 = sub(c1, mul(q, d1));
        r2 = sub(c2, mul(q, d2));
        c = d;
        c1 = d1;
        c2 = d2;
        d = r;
        d1 = r1;
        d2 = r2;
    g = n(c)
    s = div(c1, mul(u(a), u(c)))
    t = div(c2, mul(u(b), u(c)))

    return g, s, t
