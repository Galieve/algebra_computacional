from sage.all import ZZ, i
from sage.functions.other import floor, ceil

from Ring import *


class GaussianIntegers(Ring):

    def __init__(self):
        super(GaussianIntegers, self).__init__()

    def one(self):
        return 1, 0

    def zero(self):
        return 0, 0

    def add(self, (a, b), (c, d)):
        return a + c, b + d

    def mul(self,(a, b), (c, d)):
        return a*c-b*d,a*d+b*c

    def opposite(self,(a,b)):
        return -a,-b

    def normal(self,(c,d)):
        if c * d > 0 or d == 0:
            return abs(c), abs(d)
        else:
            return abs(d), abs(c);

    def quo_rem(self,(a, b), (c, d)):
        r = (a * c + b * d) / (c * c + d * d)
        s = (b * c - a * d) / (c * c + d * d)
        if abs(r - floor(r)) > 0.5:
            m = ceil(r)
        else:
            m = floor(r)
        if abs(s - floor(s)) > 0.5:
            n = ceil(s)
        else:
            n = floor(s)
        return (m, n), (a - m * c + n * d, b - m * d - n * c)

    def get_true_value(self):
        return ZZ[i]