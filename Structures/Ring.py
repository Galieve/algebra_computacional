from abc import ABCMeta, abstractmethod

from Algorithms.Chinese import chinese_reminder
from Algorithms.Euclides import euclides, extended_euclides
from Algorithms.IrreducibilityTest import repeated_squaring


class Ring:
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Ring, self).__init__()

    @abstractmethod
    def one(self):
        pass

    @abstractmethod
    def zero(self):
        pass

    @abstractmethod
    def add(self, a, b):
        pass

    def sub(self, a, b):
        return self.add(a, self.opposite(b))

    @abstractmethod
    def mul(self, a, b):
        pass

    @abstractmethod
    def quo_rem(self, a, b):
        pass

    def quo(self, a, b):
        q, _ = self.quo_rem(a, b)
        return q

    def mod(self, a, b):
        #print(type(self), a, b)
        _, m = self.quo_rem(a, b)
        return m

    @abstractmethod
    def opposite(self, a):
        pass

    @abstractmethod
    def normal(self, a):
        pass

    def unit_normal(self, a):
        if a == self.zero():
            return self.one()
        else:
            return self.quo(a, self.normal(a))

    def phi(self, a, b):
        return self.mod(b, a)

    # used mainly in exercise 3
    @abstractmethod
    def get_true_value(self):
        pass

    def reciprocal(self, a, n):
        mcd, x, y = self.extended_euclides(a, n)
        assert (mcd == self.one())
        return self.mod(x, n)

    def gcd(self,a,b):
        return self.euclides(a,b)

    def euclides(self, a, b):
        return euclides(a, b, self.normal, self.mod, self.zero)

    def extended_euclides(self, a, b):
        return extended_euclides(a, b, self.normal, self.unit_normal, self.quo, self.mul, self.sub, self.zero,
                                 self.one);

    def chinese_reminder(self, m_list, u_list):
        return chinese_reminder(m_list, u_list, self.phi, self.reciprocal, self.mul, self.add, self.sub)

    def repeated_squaring(self,a, n):
        return repeated_squaring(a, n, self)