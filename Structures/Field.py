from Algorithms.DiscreteLogarithm import discrete_logarithm, discrete_logarithm_n
from Ring import Ring
from abc import ABCMeta, abstractmethod


class Field(Ring):

    @abstractmethod
    def inverse(self, a):
        pass

    def normal(self, a):
        if a == self.zero():
            return self.zero()
        else:
            return self.one()

    def discrete_logarithm(self, a, b):
        return discrete_logarithm(a, b, self)

    def discrete_logarithm_n(self, a ,b, n):
        return discrete_logarithm_n(a, b, self, n)

    def multiplicative_order(self, n):
        if n == self.zero():
            return 0
        elif n == self.one():
            return 1
        q = self.get_order()
        acum = n
        for i in range(2, q):
            acum = self.mul(acum, n)
            if acum == self.one():
                return i