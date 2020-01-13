import Field


class QuotientFiniteField(Field.Field):

    _R = None;

    _f = None

    def __init__(self, R, f):
        super(QuotientFiniteField, self).__init__()
        self._R = R
        self._f = f

    def one(self):
        return self._R.one()

    def zero(self):
        return self._R.zero()

    def add(self, a, b):
        return self._R.mod(self._R.add(a, b), self._f)

    def mul(self, a, b):
        return self._R.mod(self._R.mul(a, b), self._f)

        # a // b == a * b^-1, en cuerpos b^-1 siempre existe.

    def quo_rem(self, a, b):
        q, m = self.quo_rem(a, b)
        return self._R.mod(q, self._f), self._R.mod(m, self._f)

    def opposite(self, a):
        return self._R.mod(a, self._f)

    def normal(self, a):
        return self._R.mod(self._R.normal(a), self._f)

    def get_true_value(self):
        pass

    def inverse(self, a):
        pass

    def get_order(self):
        return self._R.get_domain().get_order() ** self._f.degree()

    def get_domain(self):
        return self._R