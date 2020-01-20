from sage.all import *
import Structures.FieldPolynomial
import Structures.Rationals
from Algorithms.SortPolynomials import graded_lexicografic_mon

def test_ideal(f, lp, S):
    if S.is_in_ideal(f, lp):
        print f, "esta en el ideal de", lp
    else:
        print f, "no esta en el ideal de", lp

Q = Structures.Rationals.Rationals()
R = Structures.FieldPolynomial.FieldPolynomial(Q, 'y')
S = Structures.FieldPolynomial.FieldPolynomial(R, 'x', graded_lexicografic_mon)
y = R.get_variable()
x = S.get_variable()

f = x*y**2 - x
lp = [x*y + 1, y**2 - 1 + S.zero()]
test_ideal(f, lp, S)

f = x**2
lp = [x**3 - 2*x*y, x**2*y - 2*y**2 + x]
test_ideal(f, lp, S)

f = 3*x**4 + 5*x**2*y**3
g = 2*x**4 + 7*x**2
lp = [x**3, x**2*y]
test_ideal(f, lp, S)
test_ideal(g, lp, S)