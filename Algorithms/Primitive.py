# Algorithms for computer algebra, Geddes

# a, b in R, R es D.F.U.
# return gcd(a, b)
def primitive_euclidean(a, b, R):
    c = R.primitive_part(a)
    d = R.primitive_part(b)
    while d != R.zero():
        r = primitive_reminder(c, d, R)
        c = d
        d = R.primitive_part(r)
    F = R.get_domain()
    gamma = F.gcd(R.cont(a), R.cont(b))
    g = R.mul(gamma, c)
    return g

# a, b in R
# return a*beta**n mod b, donde beta == R.lc(b)
def primitive_reminder(a, b, R):
    if b == R.zero():
        return a
    beta = R.lc(b)
    n = R.degree(a) - R.degree(b) + 1
    r = R.mod(R.mul(a, R.repeated_squaring(beta, n)), b)
    return r
