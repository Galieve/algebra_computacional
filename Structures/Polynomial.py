from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

from Algorithms.Berlekamp import berlekamp_full
from Algorithms.FiniteFieldFactorization import sfd, distinct_degree_decomposition, \
    equal_degree_full_splitting
from Algorithms.IrreducibilityTest import is_irreducible
from Algorithms.Primitive import primitive_euclidean
from Structures import Field
from Structures.Ring import Ring


class Polynomial(Ring):
    R = None
    P = None

    def __init__(self, F, var):
        super(Polynomial, self).__init__()
        self.R = F
        self.P = PolynomialRing(F.get_true_value(), name=var)

    def one(self):
        return 1 + 0 * self.get_variable()

    def zero(self):
        return 0 + 0 * self.get_variable()

    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

    def quo_rem(self, a, b):
        return a.quo_rem(b)

    def opposite(self, a):
        return -a

    # normal(a) == a si el leading_coefficient de a es > 0, sino es -a
    # cuidao!
    def normal(self, a):
        if a == self.zero():
            return a
        l = a.list()
        n = self.R.normal(l[-1])
        pos = self.R.quo(n, l[-1])
        return pos * a

    def cont(self, f):
        l = [k for v, k in f.dict().items()]
        # len(l) == 0 => f == 0
        if len(l) == 0:
            return 0
        sol = self.R.normal(l[0])

        for i in range(1, len(l)):
            sol = self.R.gcd(sol, l[i])
        return sol

    def primitive_part(self, f):
        l = [k for v, k in f.dict().items()]
        c = self.cont(f)
        if c == 0: return 0
        q, _ = f.quo_rem(c)
        x = self.unit_normal(f)
        q, _ = q.quo_rem(x)
        return q

    def gcd(self, a, b):
        # cuidao
        if issubclass(type(self.R), Field.Field):
            return super(Polynomial, self).gcd(a, b)
        else:
            return primitive_euclidean(a, b, self)

    def get_variable(self):
        (var,) = self.P.gens()
        return var

    def get_true_value(self):
        return self.P

    def get_domain(self):
        return self.R

    def is_irreducible(self, f):
        return self._finite_field_is_irreducible_(f)

    def _finite_field_is_irreducible_(self, f):
        return is_irreducible(f, self)

    # solo para polinomios en cuerpos finitos.
    def pth_root(self, f, p):
        lf = f.list()
        l = []
        for i in range(0, len(lf), p):
            l.append(lf[i])
        return self.P(l)

    def derivate(self, f):
        lf = f.list()
        l = []
        for i in range(1, len(lf)):
            l.append(lf[i] * i)
        return self.P(l)

    def square_free_decomposition(self, f):
        f = self.normal(f)
        return sfd(f, self)

    def distinct_degree_decomposition(self, f):
        return distinct_degree_decomposition(f, self)

    def random_element_lim(self, a, b):
        return self.P.random_element(degree=(a, b))

    def random_element(self, n):
        return self.P.random_element(degree=(0, n))

    def equal_degree_splitting(self, f, d, k):
        return equal_degree_full_splitting(f, d, self, k)

    def berlekamp(self, f, k):
        return berlekamp_full(f, self, k)
