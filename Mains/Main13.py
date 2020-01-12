from sage.all import *
import Structures.Polynomial
import Structures.Rationals
from Algorithms.SortPolynomials import graded_lexicografic_mon

Q = Structures.Rationals.Rationals()
R = Structures.Polynomial.Polynomial(Q, 'y')
S = Structures.Polynomial.Polynomial(R, 'x', graded_lexicografic_mon)
y = R.get_variable()
x = S.get_variable()
lp = [x**3 - 2*x*y, x**2*y - 2*y**2 + x]
print S.buchberger_algorithm(lp)

Q = Structures.Rationals.Rationals()
R = Structures.Polynomial.Polynomial(Q, 'y')
S = Structures.Polynomial.Polynomial(R, 'x')
T = Structures.Polynomial.Polynomial(S, 'v')
U = Structures.Polynomial.Polynomial(T, 'u')
x = S.get_variable()
y = R.get_variable()
v = T.get_variable()
u = U.get_variable()
lp = [u*y - v*x - v, u*y - v*x + 2*v - y]
print U.buchberger_algorithm(lp)