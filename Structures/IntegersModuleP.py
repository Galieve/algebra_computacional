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
        import sage.rings.integer
        if issubclass(type(a), sage.rings.integer.Integer):
            a = int(a)
        elif not (issubclass(type(a), Ring)) and not (issubclass(type(a), int)):
            a = a.lift()

        gcd, coeff, _ = Integers().extended_euclides(a, self.p)
        assert (gcd == 1)
        return self.canonical(coeff)

    def one(self):
        return 1

    def zero(self):
        return 0

    def add(self, a, b):
        return (self.canonical(a) + self.canonical(b)) % self.p;

    def mul(self, a, b):
        return (self.canonical(a) * self.canonical(b)) % self.p

    def quo_rem(self, a, b):
        return self.mul(a, self.inverse(b)), self.zero()

    def opposite(self, a):
        return (-a + self.p) % self.p

    def canonical(self, a):
        if a < 0:
            b = self.opposite(a) % self.p
            a = self.opposite(b)
        return (a + self.p) % self.p

    def normal(self, a):
        return super(IntegersModuleP, self).normal(self.canonical(a));

    def get_true_value(self):
        return IntegerModRing(self.p)

    def get_order(self):
        return self.p

    # no funciona bien si sup >= p
    def get_random(self, inf=None, sup=None):
        import Structures.Integers
        Z = Structures.Integers.Integers()
        return Z.get_random(inf, sup) % self.p