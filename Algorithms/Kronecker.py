# Introduction to Computer Algebra (Kruger and Lossen)

from Algorithms import MathAuxiliar
from Algorithms.MathAuxiliar import get_divisors
from sage.matrix.all import Matrix
from sage.all import *

# a = [ai = [aij]], b = [bi]
# return [ai + [b]]
def cartesian_product(a, b):
    l = []
    for i in a:
        for j in b:
            k = list(i)
            k.append(j)
            l.append(k)
    return l


def generate_matrix(al, n):
    l = []
    for a in al:
        bl = [1] * (n + 1)
        for i in range(1, n + 1):
            bl[i] = a * bl[i - 1]
        l.append(bl)
    return Matrix(l)

# l lista de enteros, sl lista en modo conjunto
# agregar un entero que no este ya en la lista.
def add_distinct(l, sl, Z):
    aux = Z.get_random()
    while aux in sl:
        aux = Z.get_random()
    l.append(aux)
    sl.add(aux)


# f in R, R == Z[X]
def kronecker(f, R):
    x = R.get_variable()
    import Structures.Rationals
    Q = Structures.Rationals.Rationals()
    import Structures.Polynomial
    RQ = Structures.Polynomial.Polynomial(Q, 'x')
    fq = RQ.get_true_value()(f.list())

    # paso 1
    Z = R.get_domain()
    a = [Z.get_random()]
    sl = set(a)
    add_distinct(a, sl, Z)

    # paso 2: (x - ai) | f ?
    f0 = R.evaluate(f, a[0])
    if f0 == 0:
        return R.sub(x, a[0])
    elif R.evaluate(f, a[1]) == 0:
        return R.sub(x, a[1])

    # paso 3: define m
    m = get_divisors(f0)
    m = [[i] for i in m]
    k = R.degree(f) // 2

    # paso 4:
    for e in range(1, k + 1):

        # paso 4.1: expand m
        fae = R.evaluate(f, a[-1])
        me = get_divisors(fae)
        mn = [- i for i in  me]
        me.extend(mn)
        m = cartesian_product(m, me)
        m_ = m
        A = generate_matrix(a, e)

        # paso 4.2: test with g
        for i in range(0, len(m_)):
            c = vector(m_[i])
            b = A.solve_right(c).list()
            g = RQ.get_true_value()(b)
            if R.degree(g) == e and RQ.mod(fq, g) == RQ.zero():
                return RQ.normal(g)
        add_distinct(a, sl, Z)

    return f


def full_kronecker(f, R):
    c = R.cont(f)
    l = []
    if c == 0:
        return [f]
    elif R.normal(f) != f:
        l.append(-1)

    if c > 1:
        l.extend(MathAuxiliar.factor(c))
    f = R.primitive_part(f)
    s = [f]
    while len(s) > 0:
        poly = s.pop()
        g = kronecker(poly, R)
        if g == poly:
            l.append(g)
        else:
            s.append(g)
            s.append(R.quo(poly, g))
    return l
