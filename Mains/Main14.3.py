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
    print ""

Z = Integers.Integers()
R = IntegerPolynomial.IntegerPolynomial(Z,'x')
S = IntegerPolynomial.IntegerPolynomial(R, 'y')
x = R.get_variable()
y = S.get_variable()

a = [x*y, x**2+y]
c = y**2
I = [2]
p = 5
l = 2
d = 5
sigma = multivariate_diophant(a, c, I, d, p, l, S)
test_mv_diophantic(a, sigma, p, l, [y-2], d, S)

a = [x*y, x**2+y]
c = x**2 + 0*y
I = [2]
p = 5
l = 2
d = 5
sigma = multivariate_diophant(a, c, I, d, p, l, S)
test_mv_diophantic(a, sigma, p, l, [y-2], d, S)

a = [x*y, x**2+y, x + y, x**7 + 3*y**2]
c = 7*y**8 - x**4*y**3 + y**2 + y + x + 1
I = [3]
p = 13
l = 6
d = 8
sigma = multivariate_diophant(a, c, I, d, p, l, S)
test_mv_diophantic(a, sigma, p, l, [y-3], d, S)

a = [x*y, x**3 + y**2*x+8]
c = y**2
I = [2]
p = 5
l = 2
d = 5
sigma = multivariate_diophant(a, c, I, d, p, l, S)
test_mv_diophantic(a, sigma, p, l, [y-2], d, S)
