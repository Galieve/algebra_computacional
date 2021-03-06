
import Structures.Polynomial
import Structures.Integers
from Algorithms.HenselLifting import hensel_full_lifting, squarefree_charzero
from Algorithms.Kronecker import full_kronecker
from Algorithms.SortPolynomials import lexicografic_mon


class IntegerPolynomial(Structures.Polynomial.Polynomial):

    def __init__(self, F, var, order=lexicografic_mon):
        assert issubclass(type(F), Structures.Integers.Integers) \
               or issubclass(type(F), Structures.IntegerPolynomial.IntegerPolynomial)
        super(IntegerPolynomial, self).__init__(F, var, order)

    def kronecker(self, f):
        return full_kronecker(f, self)

    def hensel_lifting(self, f):
        return hensel_full_lifting(f, self)

    def square_free_part(self, f):
        assert self.get_order() == 0
        return squarefree_charzero(f, self)

    def symmetric_module(self, a, pl):
        import IntegersModuleP
        IMP = IntegersModuleP.IntegersModuleP(pl)
        al = self.generate_tuple_representation(a)
        l = []
        plm = pl // 2
        for m, col in al:
            mc = IMP.canonical(m)
            if mc > plm:
                mc = mc - pl
            l.append((mc, col))
        return self.generate_polynomial(l)
