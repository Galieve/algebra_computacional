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
