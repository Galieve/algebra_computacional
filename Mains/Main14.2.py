from sage.all import *

import Structures.IntegerPolynomial as IntegerPolynomial
import Structures.Polynomial as Polynomial
import Structures.Integers as Integers
import Structures.IntegersModuleP
from Algorithms.MultivariateDiophant import univariate_diophant, multivariate_diophant


def test_mv_diophantic(a, sigma, p, k, lm, d, R):
    Z = Integers.Integers()
    pk = Z.repeated_squaring(p, k)
    A = R.prod_list(a)
    b = []
    for i in a:
        b.append(R.quo(A, i))

    sum = R.zero()
    for i in range(0, len(a)):
        sum = R.add(sum, R.mul(b[i], sigma[i]))
    sumt = sum
    for j in range(0, d+2):
        sum = sumt
        for i in lm:
            sum = R.mod(sum, R.repeated_squaring(i,j))
        print "deg =", j, "moduled:", R.symmetric_module(sum, pk)
    print "suma: ", sumt
    print "sigma:", sigma

Z = Integers.Integers()
R = IntegerPolynomial.IntegerPolynomial(Z,'x')
S = IntegerPolynomial.IntegerPolynomial(R, 'y')
x = R.get_variable()
y = S.get_variable()


#print Q.gcd(f,g)
#print Q.primitive_part(f)
#print Q.primitive_part(g)
# a = [3*y**3 + 5*y**2 +  3*y + 5, 2*y**2+3]
a = [x*y, x**2+y]
c = y**2
I = [2]
sigma = multivariate_diophant(a, c, I, 5, 5, 2, S)
test_mv_diophantic(a, sigma, 5, 2, [y-2], 5, S)
