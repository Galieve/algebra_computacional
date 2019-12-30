import Field


class QuotientFiniteField(Field.Field):

    R = None;

    f = None

    def __init__(self, R, f):
        super(QuotientFiniteField, self).__init__()
        self.R = R
        self.f = f

    def one(self):
        return self.R.one()

    def zero(self):
        return self.R.zero()

    def add(self, a, b):
        return self.R.mod(self.R.add(a, b), self.f)

    def mul(self, a, b):
        return self.R.mod(self.R.mul(a, b), self.f)

        # a // b == a * b^-1, en cuerpos b^-1 siempre existe.

    def quo_rem(self, a, b):
        q, m = self.quo_rem(a, b)
        return self.R.mod(q, self.f), self.R.mod(m, self.f)

    def opposite(self, a):
        return self.R.mod(a, self.f)

    def normal(self, a):
        return self.R.mod(self.R.normal(a), self.f)

    def get_true_value(self):
        pass

    def inverse(self, a):
        pass

    def get_order(self):
        return self.R.get_domain().get_order()**self.f.degree()