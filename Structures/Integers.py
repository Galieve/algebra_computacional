from sage.all import ZZ

from Ring import *


class Integers(Ring):

    def __init__(self):
        super(Integers,self).__init__()

    def one(self):
        return 1

    def zero(self):
        return 0

    def add(self,a, b):
        return a+b

    def mul(self,a, b):
        return a*b

    def quo_rem(self,a, b):
        q = a // b
        return q, a - q*b

    def mod(self, a, b):
        return a%b

    def opposite(self, a):
        return -a

    def normal(self, a):
        if a >= 0:
            return a
        else:
            return self.opposite(a)

    def get_true_value(self):
        return ZZ

