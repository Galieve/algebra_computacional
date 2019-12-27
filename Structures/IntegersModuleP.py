from sage.rings.finite_rings.integer_mod_ring import IntegerModRing
# from sage.rings.finite_rings.integer_mod import *
from Field import Field, Ring
from Integers import Integers


class IntegersModuleP(Field):

    p = None;

    def __init__(self, p):
        super(IntegersModuleP, self).__init__()
        self.p = p;

    def inverse(self, a):
        if not(issubclass(type(a), Ring)) and not(issubclass(type(a), int)):
            a = a.lift()

        gcd, coeff, _ = Integers().extended_euclides(a, self.p)
        assert(gcd == 1)
        return self.canonical(coeff)

    def one(self):
        return 1

    def zero(self):
        return 0

    def add(self, a, b):
        return (a + b) % self.p;

    def mul(self, a, b):
        return (a * b) % self.p

    def quo_rem(self, a, b):
        return self.mul(a, self.inverse(b)), self.zero()

    def opposite(self, a):
        return (-a + self.p) % self.p

    def canonical(self, a):
        if a < 0:
            b = self.opposite(a) % self.p
            a = self.opposite(b)
        return self.add(a, self.p) % self.p

    def normal(self, a):
        return super(IntegersModuleP, self).normal(self.canonical(a));

    def multiplicative_order(self, n):
        if n == self.zero():
            return 0
        elif n == self.one():
            return 1
        acum = n
        for i in range(2, self.p):
            acum = self.mul(acum, n)
            if acum == self.one():
                return i

    def get_true_value(self):
        return IntegerModRing(self.p)
