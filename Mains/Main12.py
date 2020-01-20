import Structures.Rationals
import Structures.FieldPolynomial
from Algorithms.SortPolynomials import graded_lexicografic_mon

Q = Structures.Rationals.Rationals()
R = Structures.FieldPolynomial.FieldPolynomial(Q, 'y')
S = Structures.FieldPolynomial.FieldPolynomial(R, 'x', graded_lexicografic_mon)
T = Structures.FieldPolynomial.FieldPolynomial(S, 'z', graded_lexicografic_mon)

y = R.get_variable()
x = S.get_variable()
z = T.get_variable()

f = x ** 2 * y + x * y ** 2 + y ** 2
lf = [x * y - 1, y ** 2 - 1 + S.zero()]
print f, "se multivide entre", lf, "con ([quo], rem):", S.multivariate_division(f, lf)

f = x**2
lf = [x**3 - 2*x*y, x**2*y - 2*y**2 + x]
print f, "se multivide entre", lf, "con ([quo], rem):", S.multivariate_division(f, lf)

f = x*y**2 + 1
lf = [x*y + 1, y + 1 + S.zero()]
print f, "se multivide entre", lf, "con ([quo], rem):", S.multivariate_division(f, lf)

f = x*y**2 - x
lf = [x*y + 1, y**2 - 1 + S.zero()]
print f, "se multivide entre", lf, "con ([quo], rem):", S.multivariate_division(f, lf)


f = x**9 + x*z*y + y*x - 9*z*x
lf = [x * y - 1 + T.zero(), z + y, y ** 2 - 1 + T.zero()]
print f, "se multivide entre", lf, "con ([quo], rem):", T.multivariate_division(f, lf)


f = x + y**2 + z**3
lf = [x + T.zero(), y + T.zero(), z]
print f, "se multivide entre", lf, "con ([quo], rem):", T.multivariate_division(f, lf)

