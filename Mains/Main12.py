import Structures.Integers
import Structures.Polynomial

Z = Structures.Integers.Integers()
R = Structures.Polynomial.Polynomial(Z, 'y')
S = Structures.Polynomial.Polynomial(R, 'x')
y = R.get_variable()
x = S.get_variable()
f = x ** 2 * y + x * y ** 2 + y ** 2
lf = [x * y - 1, y ** 2 - 1 + S.zero()]
print S.multivariable_division(f, lf)
