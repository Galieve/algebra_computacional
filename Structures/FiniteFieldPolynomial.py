
import Structures.FieldPolynomial
import Structures.FiniteFields
import Structures.FiniteFieldsWrapper
from Algorithms.Berlekamp import berlekamp_full
from Algorithms.FiniteFieldFactorization import sfd, distinct_degree_decomposition, equal_degree_full_splitting
from Algorithms.IrreducibilityTest import is_irreducible
from Algorithms.SortPolynomials import lexicografic_mon


class FiniteFieldPolynomial(Structures.FieldPolynomial.FieldPolynomial):

    def __init__(self, F, var, order=lexicografic_mon):
        assert issubclass(type(F), Structures.FiniteFieldsWrapper.FiniteFieldsWrapper) \
               or issubclass(type(F), Structures.FiniteFields.FiniteFields) \
               or issubclass(type(F), Structures.FiniteFieldPolynomial.FiniteFieldPolynomial)
        super(FiniteFieldPolynomial, self).__init__(F, var, order)

    def pth_root(self, f, p):
        lf = f.list()
        l = []
        for i in range(0, len(lf), p):
            l.append(lf[i])
        return self._P(l)

    def square_free_decomposition(self, f):
        f = self.normal(f)
        return sfd(f, self)

    def distinct_degree_decomposition(self, f):
        return distinct_degree_decomposition(f, self)

    def equal_degree_splitting(self, f, d, k):
        return equal_degree_full_splitting(f, d, self, k)

    def berlekamp(self, f, k):
        return berlekamp_full(f, self, k)

    def is_irreducible(self, f):
        return is_irreducible(f, self)