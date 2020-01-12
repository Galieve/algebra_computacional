import Structures.Rationals
import Structures.FieldPolynomial

Q = Structures.Rationals.Rationals()
R = Structures.FieldPolynomial.FieldPolynomial(Q, 'y')
S = Structures.FieldPolynomial.FieldPolynomial(R, 'x')
y = R.get_variable()
x = S.get_variable()
f = x ** 2 * y + x * y ** 2 + y ** 2
lf = [x * y - 1, y ** 2 - 1 + S.zero()]
print S.multivariate_division(f, lf)
