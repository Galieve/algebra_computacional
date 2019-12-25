from sage.rings.finite_rings.finite_field_constructor import GF

from Structures.Polynomial import Polynomial
from Structures.Field import Field
from Structures.IntegersModuleP import IntegersModuleP


class FiniteFields(Field):
    # galoisField = None

    module = None

    var = None

    Poly_ring = None

    p = None

    k = None

    def __init__(self, p, k, var, poly):
        super(FiniteFields, self).__init__()
        assert (k == poly.degree())
        self.module = poly
        self.p = p
        self.k = k
        self.Poly_ring = Polynomial(IntegersModuleP(p), var)
        self.var = self.Poly_ring.get_true_value().gen()

    def __init__(self, p, k, var):
        super(FiniteFields, self).__init__()
        self.Poly_ring = Polynomial(IntegersModuleP(p), var)
        self.module = GF(p ** k, name=var).modulus();
        self.k = k
        self.module = self.module.change_ring(IntegersModuleP(p).get_true_value());
        self.module = self.module.change_variable_name(var)

        self.p = p
        self.var = self.Poly_ring.get_variable()

    def inverse(self, a):
        gcd, coeff, _ = self.Poly_ring.extended_euclides(a, self.module())
        return self.Poly_ring.mod(coeff, self.module())

    def one(self):
        return 1 + 0 * self.get_variable()

    def zero(self):
        # (a*b).rem(q)
        return 0 + 0 * self.get_variable()

    def add(self, a, b):
        return self.Poly_ring.mod(self.Poly_ring.add(a, b), self.module)

    def mul(self, a, b):
        return self.Poly_ring.mod(self.Poly_ring.mul(a, b), self.module)

        # a // b == a * b^-1, en cuerpos b^-1 siempre existe.
    def quo_rem(self, a, b):
        return self.mul(a, self.inverse(b)), self.zero()

    def opposite(self, a):
        return self.Poly_ring.mod(self.Poly_ring.opposite(a), self.module)

    def normal(self, a):
        return super(FiniteFields, self).normal(self.Poly_ring.mod(a, self.module))

    def get_variable(self):
        return self.var

    def get_true_value(self):
        # return GF(self.p**self.module.degree(),name = self.var)
        return self.Poly_ring.get_true_value()

    def get_order(self):
        return self.p**self.k

    def get_char(self):
        return self.p