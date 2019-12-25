from sage.all import *

import Structures.Polynomial
import Structures.FiniteFields

K = Structures.FiniteFields.FiniteFields(2,1, 'a')
a = K.get_variable()
R = Structures.Polynomial.Polynomial(K, 'x')
x = R.get_variable()
f = x**4 + x + 1
g = x**2 + 1 # (x+1)**2
h = x**4 + 1 # (x**2+1)**2 = (x+1)**4

print(R.is_irreducible(f))
print(R.is_irreducible(g))
print(R.is_irreducible(h))

K = Structures.FiniteFields.FiniteFields(3,3, 'a')
a = K.get_variable()
R = Structures.Polynomial.Polynomial(K, 'x')
x = R.get_variable()
i = x**2 + 1
j = x**4 + 1 # (x**2+x+2)*(x**2+2*x+2)

print(R.is_irreducible(i))
print(R.is_irreducible(j))
# x128 + x7 + x2 + x + 1.
