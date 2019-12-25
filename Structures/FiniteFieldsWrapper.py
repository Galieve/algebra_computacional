from sage.rings.finite_rings.finite_field_constructor import GF

from Structures.Field import Field


class FiniteFieldsWrapper(Field):

    galoisField = None

    p = None

    k = None

    def __init__(self, p, k, var):
        super(FiniteFieldsWrapper, self).__init__()
        self.p = p
        self.k = k
        self.galoisField = GF(p**k, name = var)

    def inverse(self, a):
        return a.inverse()

    def one(self):
        return 1 + 0 * self.get_variable()

    def zero(self):
        # (a*b).rem(q)
        return 0 + 0 * self.get_variable()

    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

        # a // b == a * b^-1, en cuerpos b^-1 siempre existe.
    def quo_rem(self, a, b):
        return a.quo_rem(b)

    def opposite(self, a):
        return -a

    def normal(self, a):
        return super(FiniteFieldsWrapper, self).normal(a)

    def get_variable(self):
        return self.galoisField.gen()

    def get_true_value(self):
        # return GF(self.p**self.module.degree(),name = self.var)
        return self.galoisField

    def get_order(self):
        return self.p**self.k