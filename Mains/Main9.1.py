import Structures.Integers
import Structures.Polynomial

Z = Structures.Integers.Integers()
R = Structures.Polynomial.Polynomial(Z, 'x')
x = R.get_variable()

f = x ** 3 - x + 1
g = x ** 2 - x - 1
j = f * g
i = x ** 2 + 2 * x + 1
k = x ** 8 + x ** 7 - x ** 6 + x ** 5 - x ** 3 - x ** 2 - x

print R.kronecker(i)
print R.kronecker(j)
print R.kronecker(k)
print R.kronecker(-j)
print R.kronecker(-64 * j)
