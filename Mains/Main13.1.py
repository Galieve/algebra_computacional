from sage.all import *
import Structures.FieldPolynomial
import Structures.Rationals
from Algorithms.SortPolynomials import graded_lexicografic_mon

Q = Structures.Rationals.Rationals()
R = Structures.FieldPolynomial.FieldPolynomial(Q, 'y')
S = Structures.FieldPolynomial.FieldPolynomial(R, 'x', graded_lexicografic_mon)
y = R.get_variable()
x = S.get_variable()
lp = [x**3 - 2*x*y, x**2*y - 2*y**2 + x]
print "Una base de Grobner es:", S.buchberger_algorithm(lp), "y la reducida es:", S.minimal_reduced_buchberger_algorithm(lp)

Q = Structures.Rationals.Rationals()
R = Structures.FieldPolynomial.FieldPolynomial(Q, 'y')
S = Structures.FieldPolynomial.FieldPolynomial(R, 'x')
T = Structures.FieldPolynomial.FieldPolynomial(S, 'v')
U = Structures.FieldPolynomial.FieldPolynomial(T, 'u')
y = R.get_variable()
x = S.get_variable()
v = T.get_variable()
u = U.get_variable()
lp = [u*y - v*x - v, u*y - v*x + 2*v - y]
print "Una base de Grobner es:", U.buchberger_algorithm(lp), "y la reducida es:", U.minimal_reduced_buchberger_algorithm(lp)


Q = Structures.Rationals.Rationals()
R = Structures.FieldPolynomial.FieldPolynomial(Q, 'x')
S = Structures.FieldPolynomial.FieldPolynomial(R, 'y')
T = Structures.FieldPolynomial.FieldPolynomial(S, 'z')
U = Structures.FieldPolynomial.FieldPolynomial(T, 't')
x = R.get_variable()
y = S.get_variable()
z = T.get_variable()
t = U.get_variable()
lp = [x - t, y - t**2, z - t**3]
print "Una base de Grobner es:", U.buchberger_algorithm(lp), "y la reducida es:", U.minimal_reduced_buchberger_algorithm(lp)


Q = Structures.Rationals.Rationals()
R = Structures.FieldPolynomial.FieldPolynomial(Q, 'x')
S = Structures.FieldPolynomial.FieldPolynomial(R, 'y')
T = Structures.FieldPolynomial.FieldPolynomial(S, 'z')
U = Structures.FieldPolynomial.FieldPolynomial(T, 't')
x = R.get_variable()
y = S.get_variable()
z = T.get_variable()
t = U.get_variable()
lp = [x - t**2, y - t**3, z - t**4]
print "Una base de Grobner es:", U.buchberger_algorithm(lp), "y la reducida es:", U.minimal_reduced_buchberger_algorithm(lp)