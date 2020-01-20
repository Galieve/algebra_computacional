# Modern Computer Algebra

from sage.matrix.all import Matrix
from sage.functions.other import sqrt, ceil

from MathAuxiliar import to_binary, factor


# a in R, n in Z
# return a**n
def repeated_squaring(a, n, R):
    if n == 0:
        return R.one()
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


# f, g, h in R, R == polynomial
# return g(h) mod f
def fast_modular_composition(f, g, h, R):
    assert (f != R.zero())
    assert (R.degree(g) < R.degree(f))
    assert (R.degree(h) < R.degree(f))

    # paso 1
    n = R.degree(f)
    m = int(ceil(sqrt(n)))
    B = []
    q = g.list()
    k = 0

    # paso 1.1: calcular B == filas formadas por g_i donde g = sum(g_i*x**(m*i))
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

    # paso 2: calcular A == filas formadas por h**i mod f
    acum = R.one()
    A = [R.zero()] * m
    for i in range(0, m):
        # R.zero() == polynomial, R.zero()[0] == element of a polynomial
        zero = [R.get_domain().zero()] * (n - len(acum.list()))
        al = acum.list()
        al.extend(zero)
        al.reverse()
        A[i] = al
        acum = R.mod(R.mul(acum, h), f)

    # paso 3: calcular B * A
    A = Matrix(A)
    B = Matrix(B)
    r = B * A

    # paso 4: calcular b = sum(r_i*h**(m*i)) mod f, r_i = fila de r = B * A
    # hm = repeated_squaring(h, m , R)
    hm = acum
    rl = r.rows()[m - 1].list()
    rl.reverse()
    sol = R.get_true_value()(rl)
    for i in range(m - 2, -1, -1):
        rl = r.rows()[i].list()
        rl.reverse()
        sol = R.mod(sol * hm + R.get_true_value()(rl), f)

    # paso 5
    return sol


# g in R, n in Z
# return [1, g, g**2, g **4,...g**(2**(n))] mod f
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


# bn == n in binary, lp = g**(q*i), f in R
# return g**n mod f
def compute_power(bn, lp, f, R):
    sol = R.get_variable()
    for i in range(0, len(bn)):
        if bn[i] == 1:
            sol = fast_modular_composition(f, sol, lp[i + 1], R)
    return sol

# f in R, R = FiniteFieldPolynomial
def is_irreducible(f, R):
    x = R.get_variable()
    import Structures.QuotientFiniteField
    QF = Structures.QuotientFiniteField.QuotientFiniteField(R, f)

    # paso 1: calcular x**q mod f y a = x**(q**n) mod f
    xq = QF.repeated_squaring(x, R.get_domain().get_order())
    n = R.degree(f)
    bn = to_binary(n)
    lp = list_of_powers(len(bn), xq, f, R)
    a = compute_power(bn, lp, f, R)
    if a != x:
        return False

    # paso 2: para todos los divisores primos de n
    s = set(factor(n))
    for i in s:

        # paso 3: calcular b = x**(q**(n/i))
        bi = to_binary(n // i)
        b = compute_power(bi, lp, f, R)
        if R.gcd(R.sub(b, x), f) != R.one():
            return False

    # paso 4: es irreducible
    return True
