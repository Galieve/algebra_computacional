import sage.rings.finite_rings.finite_field_constructor

from Structures.Field import Field


class FiniteFieldsWrapper(Field):

    _galoisField = None

    _p = None

    _k = None

    def __init__(self, p, k, var):
        super(FiniteFieldsWrapper, self).__init__()
        self._p = p
        self._k = k
        self._galoisField = sage.rings.finite_rings.finite_field_constructor.GF(p ** k, name = var)

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
        return self._galoisField.gen()

    def get_true_value(self):
        # return GF(self.p**self.module.degree(),name = self.var)
        return self._galoisField

    def get_order(self):
        return self._p ** self._k

    def get_random(self, inf = None, sup = None):
        return self._galoisField.random_element()