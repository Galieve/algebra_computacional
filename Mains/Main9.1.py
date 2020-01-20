import Structures.Integers
import Structures.IntegerPolynomial

Z = Structures.Integers.Integers()
R = Structures.IntegerPolynomial.IntegerPolynomial(Z, 'x')
x = R.get_variable()

f = x ** 3 - x + 1
g = x ** 2 - x - 1
j = f * g
i = x ** 2 + 2 * x + 1
k = x ** 8 + x ** 7 - x ** 6 + x ** 5 - x ** 3 - x ** 2 - x
l = 2*x**2 + 3*x

print i, "factoriza como:", R.kronecker(i)
print j, "factoriza como:", R.kronecker(j)
print k, "factoriza como:", R.kronecker(k)
print -j, "factoriza como:", R.kronecker(-j)
print -64*j, "factoriza como:", R.kronecker(-64 * j)
print l, "factoriza como:", R.kronecker(l)
