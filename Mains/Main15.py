from sage.all import *

import Structures.IntegerPolynomial as IntegerPolynomial
import Structures.Polynomial as Polynomial
import Structures.Integers as Integers
import Structures.IntegersModuleP
from Algorithms.MultivariateDiophant import univariate_diophant, multivariate_diophant
from Algorithms.MultivariateHenselLifting import multivariate_hensel_lifting


def test_diophantic(a, sigma, p, k):
    Z = Integers.Integers()
    pk = Z.repeated_squaring(p, k)
    A = R.prod_list(a)
    b = []
    for i in a:
        b.append(R.quo(A, i))

    sum = R.zero()
    for i in range(0, len(a)):
        sum = R.add(sum, R.mul(b[i], sigma[i]))
    print "suma:", sum, "moduled:", R.symmetric_module(sum, pk), "sigma:", sigma

Z = Integers.Integers()
R = IntegerPolynomial.IntegerPolynomial(Z,'x')
S = IntegerPolynomial.IntegerPolynomial(R, 'y')
T = IntegerPolynomial.IntegerPolynomial(S, 'z')
x = R.get_variable()
y = S.get_variable()
z = T.get_variable()

a = x**2*y**4*z - x*y*z**2 + x*y*z**3 + 2*x - y*z**4 - 2*y*z
I = [1, 1]
p = 5
l = 1
ul = [x - 2, x - 1]
lcul = [1, 1]

# aux = [5*x - 5, 4*x**2 - 8*x - 16, 6*x**2 - 36*x - 35, 4*x**2 - 84*x - 40, x**2 - 126*x - 25, -126*x - 8, -84*x - 1, -36*x, -9*x, -x]
# mon = y - 1
# mul = 1
# sum = 0
# for i in aux:
#     sum = sum + i * mul
#     mul = mul * mon
# print sum
# -x*y^9 - y^6 - 2*y^5 + x^2*y^4 + x*y - x^2 + 5*x - 2
print multivariate_hensel_lifting(a, T, I, p, l, ul, lcul)
