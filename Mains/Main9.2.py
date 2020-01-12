import Structures.Integers
import Structures.IntegerPolynomial

Z = Structures.Integers.Integers()
R = Structures.IntegerPolynomial.IntegerPolynomial(Z, 'x')
x = R.get_variable()
f = x ** 3 - x + 1
g = x ** 2 - x - 1
j = f * g
i = x**2 + 2 * x + 1
k = x ** 8 + x ** 7 - x ** 6 + x ** 5 - x ** 3 - x ** 2 - x
l = 2*x**2 + 3*x

i = R.square_free_part(i)
print R.hensel_lifting(i)
print R.hensel_lifting(j)
print R.hensel_lifting(k)
print R.hensel_lifting(-j)
print R.hensel_lifting(-64 * j)
print R.hensel_lifting(l)