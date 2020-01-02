from sage.all import QQ
from Structures.Field import Field


class Rationals(Field):


    def __init__(self):
        super(Rationals, self).__init__()

    def inverse(self, a):
        return 1 / a

    def one(self):
        return 1

    def zero(self):
        # (a*b).rem(q)
        return 0

    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

        # a // b == a * b^-1, en cuerpos b^-1 siempre existe.
    def quo_rem(self, a, b):
        return a / b, 0

    def opposite(self, a):
        return - a

    def normal(self, a):
        return super(Rationals, self).normal(a)

    def get_true_value(self):
        # return GF(self.p**self.module.degree(),name = self.var)
        return QQ

    def get_char(self):
        return 0

    def get_order(self):
        return - 1