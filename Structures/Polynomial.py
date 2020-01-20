from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

from Algorithms.Primitive import primitive_euclidean
from Algorithms.SortPolynomials import sort_polynomials, lexicografic_mon
from Structures import Field
from Structures.Ring import Ring


class Polynomial(Ring):
    _R = None

    _P = None

    _order = None

    _num_variables = None

    def __init__(self, F, var, order=lexicografic_mon):
        super(Polynomial, self).__init__()
        self._R = F
        self._P = PolynomialRing(F.get_true_value(), name=var)
        self._order = order
        if issubclass(type(F), Polynomial):
            self._num_variables = F._num_variables + 1
        else:
            self._num_variables = 1

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

    def get_order(self):
        return self.get_domain().get_order()

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

    def get_bottom_domain(self):
        if issubclass(type(self._R), Polynomial):
            return self._R.get_bottom_domain()
        else:
            return self._R

    def number_of_variables(self):
        return self._num_variables

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

    # Si f \in F[x1, ..., xn], f = a0*x**alpha0 + ..., con alpha0 vector
    # entonces deep_lc(f) = an, con n el mayor de ellos xD
    def recursive_lc(self, f):
        if f == self.zero():
            return f
        lt = self.lt(f)
        return self._recursive_lc_(lt)

    # El lc de un polinomio multivariable esta en una dimension menor
    def lc(self, f):
        if f == self.zero():
            return f
        lt = self.lt(f)
        l = lt.list()
        return l[-1]

    def _recursive_lc_(self, lt):
        if issubclass(type(self._R), Polynomial):
            l = lt.list()
            return self._R._recursive_lc_(l[-1])
        else:
            l = lt.list()
            return l[-1]

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

    def random_element_lim(self, a, b):
        return self._P.random_element(degree=(a, b))

    def random_element(self, n):
        return self._P.random_element(degree=(0, n))

    # solo con respecto a la variable mas externa
    def derivate(self, f):
        lf = f.list()
        l = []
        for i in range(1, len(lf)):
            l.append(self._R.mul(lf[i], i))
        return self._P(l)

    def evaluate(self, f, a):
        if f == self.zero():
            return 0
        fl = f.list()
        result = fl[-1]
        for i in range(len(fl) - 2, -1, -1):
            result = self._R.add(self._R.mul(result, a), fl[i])
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

    def prod_list(self, l):
        prod = self.one()
        # tipos!
        for i in l:
            prod = self.mul(prod, i)
        return prod

    # a y b son vectores (listas) con coeficientes en self
    # el input "viene" de un dominio superior y el ouput vive en self
    def prod_esc(self, a, b):
        assert len(a) == len(b)
        sol = self.zero()
        for i in range(0, len(a)):
            sol = self.add(sol, self.mul(a[i], b[i]))
        return sol

    def p_adic_taylor_series(self, f, g):
        pol = f
        l = []
        c = -g.list()[0]
        while pol != self.zero():
            m = self.evaluate(pol, c)
            l.append(m)
            pol = self.quo(self.sub(pol, m), g)
        return l
