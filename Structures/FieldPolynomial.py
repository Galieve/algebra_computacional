
import Structures.Polynomial
import Structures.Field
from Algorithms.Buchberger import buchberger_algorithm
from Algorithms.HenselLifting import squarefree_charzero
from Algorithms.MultivariateDivision import multivariate_division
from Algorithms.SortPolynomials import lexicografic_mon


class FieldPolynomial(Structures.Polynomial.Polynomial):

    def __init__(self, F, var, order=lexicografic_mon):
        assert issubclass(type(F), Structures.Field.Field) \
               or issubclass(type(F), Structures.FieldPolynomial.FieldPolynomial)
        super(FieldPolynomial, self).__init__(F, var, order)


    def multivariate_division(self, f, lf):
        return multivariate_division(f, lf, self)

    def buchberger_algorithm(self, lp):
        return buchberger_algorithm(lp, self)

    def square_free_part(self, f):
        assert self.get_order() == 0
        return squarefree_charzero(f, self)
