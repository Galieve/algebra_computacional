from Structures.QuotientFiniteField import QuotientFiniteField
from sage.matrix.all import Matrix

def berlekamp1_3(f, R):
    # paso 1
    q = R.get_domain().get_order()
    x = R.get_variable()
    n = R.degree(f)
    assert (q % 2 != 0)
    QF = QuotientFiniteField(R, f)
    xq = QF.repeated_squaring(x, q)

    # paso 2
    fl = f.list()
    Q = []
    acum = R.one()
    for i in range(0, n):
        al = acum.list()
        zero = [R.get_domain().zero()] * (n - len(al))
        al.extend(zero)
        #al.reverse()
        Q.append(al)
        acum = QF.mul(xq, acum)

    # paso 3
    Q = Matrix(Q)
    I = Matrix.identity(n)
    QI = Q - I
    kqi = QI.kernel().basis_matrix().rows()
    r = len(kqi)
    bl = []
    for ro in kqi:
        # cuidao
        #ro.reverse()
        bl.append(R.get_true_value()(ro.list()))
    return r, bl

def berlekamp4_7(f, R, r, bl):
    q = R.get_domain().get_order()
    QF = QuotientFiniteField(R, f)
    if r == 1:
        return f

    # paso 4
    cl = []
    for i in range(0, r):
        cl.append(R.get_domain().get_random())
    al = [cl[k] * bl[k] for k in range(0, r)]
    a = R.zero()
    for a_ in al:
        a = R.add(a, a_)

    a = R.get_true_value()(a)

    # paso 5
    g1 = R.gcd(a, f)
    if g1 != R.one() and g1 != f:
        return g1

    # paso 6
    exp = (q - 1)//2
    b = QF.repeated_squaring(a, exp)

    # paso 7
    g2 = R.gcd(R.sub(b, R.one()), f)
    if g2 != R.one() and g2 != f:
        return g2
    else:
        return None

def berlekamp_k_times(f, R, k):
    r, bl = berlekamp1_3(f, R)
    if r == 1:
        return f
    for i in range(0, k):
        p = berlekamp4_7(f, R, r, bl)
        if p is not None:
            return p
    return None

def berlekamp_full(f, R, k):
    g = berlekamp_k_times(f, R, k)
    if g is None:
        return None
    elif g == f:
        return [f]
    gl = berlekamp_full(g, R, k)
    fl = berlekamp_full(R.quo(f, g), R, k)
    gl.extend(fl)
    return gl
