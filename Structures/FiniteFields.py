from sage.rings.finite_rings.finite_field_constructor import GF

from Structures.Polynomial import Polynomial
from Structures.Field import Field
from Structures.IntegersModuleP import IntegersModuleP


class FiniteFields(Field):
    # galoisField = None

    _module = None

    _var = None

    _Poly_ring = None

    _p = None

    _k = None

    def __init__(self, p, k, var, poly):
        super(FiniteFields, self).__init__()
        assert (k == poly.degree())
        self._module = poly
        self._p = p
        self._k = k
        self._Poly_ring = Polynomial(IntegersModuleP(p), var)
        self._var = self._Poly_ring.get_true_value().gen()

    def __init__(self, p, k, var):
        super(FiniteFields, self).__init__()
        self._Poly_ring = Polynomial(IntegersModuleP(p), var)
        self._module = GF(p ** k, name=var).modulus();
        self._k = k
        self._module = self._module.change_ring(IntegersModuleP(p).get_true_value());
        self._module = self._module.change_variable_name(var)

        self._p = p
        self._var = self._Poly_ring.get_variable()

    def inverse(self, a):
        gcd, coeff, _ = self._Poly_ring.extended_euclides(a, self._module())
        return self._Poly_ring.mod(coeff, self._module())

    def one(self):
        return 1 + 0 * self.get_variable()

    def zero(self):
        # (a*b).rem(q)
        return 0 + 0 * self.get_variable()

    def add(self, a, b):
        return self._Poly_ring.mod(self._Poly_ring.add(a, b), self._module)

    def mul(self, a, b):
        return self._Poly_ring.mod(self._Poly_ring.mul(a, b), self._module)

        # a // b == a * b^-1, en cuerpos b^-1 siempre existe.
    def quo_rem(self, a, b):
        return self.mul(a, self.inverse(b)), self.zero()

    def opposite(self, a):
        return self._Poly_ring.mod(self._Poly_ring.opposite(a), self._module)

    def normal(self, a):
        return super(FiniteFields, self).normal(self._Poly_ring.mod(a, self._module))

    def get_variable(self):
        return self._var

    def get_true_value(self):
        # return GF(self.p**self.module.degree(),name = self.var)
        return self._Poly_ring.get_true_value()

    def get_order(self):
        return self._p ** self._k

    def get_char(self):
        return self._p

    def get_random(self, inf=None, sup=None):
        return self.get_true_value().random_element(inf, sup)