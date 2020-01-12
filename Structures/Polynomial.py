from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

from Algorithms.Berlekamp import berlekamp_full
from Algorithms.Buchberger import buchberger_algorithm
from Algorithms.FiniteFieldFactorization import sfd, distinct_degree_decomposition, \
    equal_degree_full_splitting
from Algorithms.HenselLifting import hensel_full_lifting
from Algorithms.Kronecker import full_kronecker
from Algorithms.IrreducibilityTest import is_irreducible
from Algorithms.MultivariateDivision import multivariate_division
from Algorithms.Primitive import primitive_euclidean
from Algorithms.SortPolynomials import sort_polynomials, lexicografic_mon
from Structures import Field
from Structures.Ring import Ring


class Polynomial(Ring):

    _R = None

    _P = None

    _order = None

    def __init__(self, F, var, order=lexicografic_mon):
        super(Polynomial, self).__init__()
        self._R = F
        self._P = PolynomialRing(F.get_true_value(), name=var)
        self._order = order

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
        lt = self.lt(a)
        lt_ = lt.list()[-1]
        n = self._R.normal(lt_)
        pos = self._R.quo(n, lt_)
        return pos * a


    def cont(self, f):
        l = [k for v, k in f.dict().items()]
        # len(l) == 0 => f == 0
        if len(l) == 0:
            return 0
        sol = self._R.normal(l[0])

        for i in range(1, len(l)):
            sol = self._R.gcd(sol, l[i])
        return sol

    def primitive_part(self, f):
        l = [k for v, k in f.dict().items()]
        c = self.cont(f)
        if c == 0: return self.zero()
        q, _ = f.quo_rem(c)
        x = self.unit_normal(f)
        q, _ = q.quo_rem(x)
        return q

    def gcd(self, a, b):
        # cuidao
        if issubclass(type(self._R), Field.Field):
            return super(Polynomial, self).gcd(a, b)
        else:
            return primitive_euclidean(a, b, self)

    def get_variable(self):
        (var,) = self._P.gens()
        return var

    def get_true_value(self):
        return self._P

    def get_domain(self):
        return self._R

    def is_irreducible(self, f):
        return self._finite_field_is_irreducible_(f)

    def _finite_field_is_irreducible_(self, f):
        return is_irreducible(f, self)

    # solo para polinomios en una variable en cuerpos finitos con el orden por defecto.
    def pth_root(self, f, p):
        lf = f.list()
        l = []
        for i in range(0, len(lf), p):
            l.append(lf[i])
        return self._P(l)

    def derivate(self, f):
        lf = f.list()
        l = []
        for i in range(1, len(lf)):
            l.append(lf[i] * i)
        return self._P(l)

    def square_free_decomposition(self, f):
        f = self.normal(f)
        return sfd(f, self)

    def distinct_degree_decomposition(self, f):
        return distinct_degree_decomposition(f, self)

    def random_element_lim(self, a, b):
        return self._P.random_element(degree=(a, b))

    def random_element(self, n):
        return self._P.random_element(degree=(0, n))

    def equal_degree_splitting(self, f, d, k):
        return equal_degree_full_splitting(f, d, self, k)

    def berlekamp(self, f, k):
        return berlekamp_full(f, self, k)

    def evaluate(self, f, a):
        if f == self.zero():
            return 0
        fl = f.list()
        result = fl[-1]
        for i in range(len(fl) - 2, -1, -1):
            result = result * a + fl[i]
        return result

    # solo para una variable
    def degree(self, f):  # cuidao
        if f == self.zero(): return 0
        return len(f.list()) - 1

    # no apto para polinomios de varias variables
    def max_norm(self, f):
        fl = f.list()
        if len(fl) == 0:
            return 0
        maxn = abs(f[0])
        for i in fl:
            maxn = max(abs(i), maxn)
        return maxn

    # no apto para polinomios de varias variables
    def one_norm(self, f):
        if f == self.zero():
            return 0
        flist = f.list()
        on = abs(flist[0])
        for i in range(1, len(flist)):
            on = self._R.add(abs(flist[i]), on)
        return on

    def kronecker(self, f):
        return full_kronecker(f, self)

    def hensel_lifting(self, f):
        return hensel_full_lifting(f, self)

    def lt(self, f):
        if f == self.zero():
            return f
        elif self._order is None:
            fl = f.list()
            if issubclass(type(self._R), Polynomial):
                l = self._R.lt(fl[-1])
            else:
                l = fl[-1]
            l = self.mul(l, self.repeated_squaring(self.get_variable(), len(fl) - 1))
            return l
        else:
            ls = self.generate_tuple_representation(f)
            ls.sort(cmp=self._order)
            return self.generate_monomial(ls[-1])

    def generate_monomial(self, (c, l)):
        if issubclass(type(self._R), Polynomial):
            sol = self._R.generate_monomial((c, l[1:]))
        else:
            sol = c
        x = self.get_variable()
        xn = self.repeated_squaring(x, l[0])
        sol = self.mul(sol, xn)
        return sol

    def generate_tuple_representation(self, f):
        l = self._generate_tuple_representation_(f)
        l_ = []
        for c, le in l:
            l_.append((c, list(le)))
        return l_

    def _generate_tuple_representation_(self, f):
        import collections
        fl = f.list()
        l = []
        for i in range(0, len(fl)):
            if fl[i] == self._R.zero():
                continue
            elif issubclass(type(self._R), Polynomial):
                ls = self._R._generate_tuple_representation_(fl[i])
                for e, le in ls:
                    le.appendleft(i)
                    l.append((e, le))
            else:
                l.append((fl[i], collections.deque([i])))
        return l

    def generate_polynomial(self, l):
        f = self.zero()
        for i in l:
            f = self.add(f, self.generate_monomial(i))
        return f

    def sort_polynomials(self, lpoly, reverse=False):
        lp = []
        for i in lpoly:
            lp.append(self.generate_tuple_representation(i))
        lp.sort(cmp=lambda a, b: sort_polynomials(a, b, self._order), reverse=reverse)
        lsol = []
        for i in lp:
            lsol.append(self.generate_polynomial(i))
        return lsol

    def multidegree(self, f):
        if f == self.zero() and not issubclass(type(self._R), Polynomial):
            return [0]
        elif f == self.zero():
            l = self._R.multidegree(self._R.zero())
            return l.append(0)
        else:
            lis = self.generate_tuple_representation(f)
            if self._order is not None:
                lis.sort(cmp=self._order)
            c, l = lis[-1]
            return l

    def multivariate_division(self, f, lf):
        return multivariate_division(f, lf, self)

    def buchberger_algorithm(self, lp):
        return buchberger_algorithm(lp, self)

