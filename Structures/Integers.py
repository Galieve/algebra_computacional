from sage.all import ZZ
import Ring
from Algorithms.AKS import AKS
from Algorithms.MillerRabin import miller_rabin


class Integers(Ring.Ring):

    def __init__(self):
        super(Integers, self).__init__()

    def one(self):
        return 1

    def zero(self):
        return 0

    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

    def quo_rem(self, a, b):
        q = a // b
        return q, a - q * b

    def mod(self, a, b):
        return a % b

    def opposite(self, a):
        return -a

    def normal(self, a):
        if a >= 0:
            return a
        else:
            return self.opposite(a)

    def get_true_value(self):
        return ZZ

    def get_random(self, inf = None, sup = None):
        if sup is not None:
            return ZZ.random_element(inf, sup + 1)
        else:
            return ZZ.random_element(inf, sup)

    def miller_rabin(self, n, k):
        return miller_rabin(n, k)

    def aks(self, a):
        return AKS(a)
