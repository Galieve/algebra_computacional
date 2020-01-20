from sage.all import *

import Structures.IntegerPolynomial as IntegerPolynomial
import Structures.Integers as Integers
from Algorithms.MultivariateDiophant import univariate_diophant


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
R = IntegerPolynomial.IntegerPolynomial(Z, 'y')
y = R.get_variable()

a = [2 * y ** 2 + 3, 3 * y + 5, y ** 2 + 1]
sigma = univariate_diophant(a, y, 2, 5, 2, R)
test_diophantic(a, sigma, 5, 2)

a = [y ** 3 + 2 * y, 2 * y ** 2 + 3]
sigma = univariate_diophant(a, y, 4, 5, 2, R)
test_diophantic(a, sigma, 5, 2)

a = [y + 1, y ** 3, 2 * y ** 3 + 3 * y ** 2 + y - 1, -7 + 0 * y]
sigma = univariate_diophant(a, y, 6, 83, 11, R)
test_diophantic(a, sigma, 83, 11)

a = [8 * y ** 7 - 5 * y ** 6 + 2, 9 * y ** 10 - 5 * y ** 6 + 4, y]
sigma = univariate_diophant(a, y, 17, 5, 2, R)
test_diophantic(a, sigma, 5, 2)
