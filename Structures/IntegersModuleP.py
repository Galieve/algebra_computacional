from sage.rings.finite_rings.integer_mod_ring import IntegerModRing
# from sage.rings.finite_rings.integer_mod import *
import Field, Ring, Integers


class IntegersModuleP(Field.Field):

    _p = None;

    def __init__(self, p):
        super(IntegersModuleP, self).__init__()
        self._p = p;

    def inverse(self, a):
        import sage.rings.integer
        if issubclass(type(a), sage.rings.integer.Integer):
            a = int(a)
        elif not (issubclass(type(a), Ring.Ring)) and not (issubclass(type(a), int)):
            a = a.lift()

        gcd, coeff, _ = Integers.Integers().extended_euclides(a, self._p)
        assert (gcd == 1)
        return self.canonical(coeff)

    def one(self):
        return 1

    def zero(self):
        return 0

    def add(self, a, b):
        return (self.canonical(a) + self.canonical(b)) % self._p;

    def mul(self, a, b):
        return (self.canonical(a) * self.canonical(b)) % self._p

    def quo_rem(self, a, b):
        return self.mul(a, self.inverse(b)), self.zero()

    def opposite(self, a):
        return (-a + self._p) % self._p

    def canonical(self, a):
        if a < 0:
            b = self.opposite(a) % self._p
            a = self.opposite(b)
        return (a + self._p) % self._p

    def normal(self, a):
        return super(IntegersModuleP, self).normal(self.canonical(a));

    def get_true_value(self):
        return IntegerModRing(self._p)

    def get_order(self):
        return self._p

    # no funciona bien si sup >= p
    def get_random(self, inf=None, sup=None):
        import Structures.Integers
        Z = Structures.Integers.Integers()
        return Z.get_random(inf, sup) % self._p