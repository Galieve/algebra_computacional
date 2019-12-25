from sage.matrix.all import Matrix
from sage.functions.other import sqrt, ceil

from MathAuxiliar import to_binary, factor



def repeated_squaring(a, n, R):
    l = to_binary(n)
    k = len(l) - 1
    b = [R.zero()] * (k + 1)
    b[k] = a
    for i in range(k - 1, -1, -1):
        if l[i] == 1:
            b[i] = R.mul(R.mul(b[i + 1], b[i + 1]), a)
        else:
            b[i] = R.mul(b[i + 1], b[i + 1])
    return b[0]


# f, g, h \in R, type(R) == Ring, issubclassof(R, Polynomial)
def fast_modular_composition(f, g, h, R):
    assert (f != R.zero())
    assert (g.degree() < f.degree())
    assert (h.degree() < f.degree())
    n = f.degree()
    m = int(ceil(sqrt(n)))
    B = []
    q = g.list()
    k = 0
    for i in range(0, m):
        cont = 0
        aux = [R.zero()] * m
        while k < len(q):
            aux[cont] = q[k]
            cont = cont + 1
            k = k + 1
            if cont == m:
                break
        B.append(aux)
    # hemos hecho el punto 1 y tenemos ya B. pag 338
    acum = R.one()
    A = [R.zero()] * m
    for i in range(0, m):
        # 0 0 1 0 1
        # R.zero() == polynomial, R.zero()[0] == element of a polynomial
        zero = [R.zero()[0]] * (n - len(acum.list()))
        al = acum.list()
        al.extend(zero)
        al.reverse()
        A[i] = al
        acum = R.mod(R.mul(acum, h), f)

    # hemos hecho el punto 2 y 3
    A = Matrix(A)
    B = Matrix(B)
    r = B * A
    # hm = repeated_squaring(h, m , R)
    # hm \in R, r[i] \in vector
    hm = acum
    rl = r.rows()[m - 1].list()
    rl.reverse()
    sol = R.get_true_value()(rl)
    for i in range(m - 2, -1, -1):
        rl = r.rows()[i].list()
        rl.reverse()
        sol = R.mod(sol * hm + R.get_true_value()(rl), f)
    return sol


# dada g obtienes [1, g, g**2, g **4,...g**(2**(n))]
def list_of_powers(n, g, f, R):
    l = [R.one()]
    aux = g
    j = 1
    while j <= n:
        l.append(aux)
        aux = fast_modular_composition(f, aux, aux, R)
        j = j + 1
    assert (len(l) == n + 1)
    return l


# dado a => x**a
# dado f, g, h => g(h) (mod f)
# x**q**n: dos maneras
# calcular(q**n) => calcular(x**q**n)
# calcular(x**q) => calcular(x**q**n)

# x**q**5, => 5 == 101,
# (x**q)(x**q**4)=(x**q**4)**q = (x**(q**4*q)) = x**q**5

def compute_power(bn, lp, f, R):
    sol = R.get_variable()
    for i in range(0, len(bn)):
        if bn[i] == 1:
            sol = fast_modular_composition(f, sol, lp[i+1], R)
    return sol


def is_irreducible(f, R):
    x = R.get_variable()
    import Structures.QuotientFiniteField
    QF = Structures.QuotientFiniteField.QuotientFiniteField(R, f)
    xq = QF.repeated_squaring(x, R.get_domain().get_order())
    n = f.degree()
    bn = to_binary(n)
    lp = list_of_powers(len(bn), xq, f, R)
    a = compute_power(bn, lp, f, R)
    if a != x:
        return False

    s = set(factor(n))
    for i in s:
        bi = to_binary(n // i)
        b = compute_power(bi, lp, f, R)
        if R.gcd(R.sub(b, x), f) != R.one():
            return False
    return True
