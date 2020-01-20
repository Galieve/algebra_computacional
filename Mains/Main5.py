from sage.all import *

import Structures.FiniteFieldPolynomial
import Structures.FiniteFields


def test_irreducible(f, R):
    p = R.get_domain().get_char()
    k = R.get_domain().get_exponent()
    if R.is_irreducible(f):
        print f, "es irreducible en F(", p, ",", k, ")"
    else:
        print f, "no es irreducible en F(", p, ",", k, ")"


K = Structures.FiniteFields.FiniteFields(2, 1, 'a')
a = K.get_variable()
R = Structures.FiniteFieldPolynomial.FiniteFieldPolynomial(K, 'x')
x = R.get_variable()
f = x ** 4 + x + 1
g = x ** 2 + 1  # (x+1)**2
h = x ** 4 + 1  # (x**2+1)**2 = (x+1)**4

test_irreducible(f, R)
test_irreducible(g, R)
test_irreducible(h, R)
print ""

K = Structures.FiniteFields.FiniteFields(3, 3, 'a')
a = K.get_variable()
R = Structures.FiniteFieldPolynomial.FiniteFieldPolynomial(K, 'x')
x = R.get_variable()
i = x ** 2 + 1
j = x ** 4 + 1  # (x**2+x+2)*(x**2+2*x+2)

test_irreducible(i, R)
test_irreducible(j, R)
