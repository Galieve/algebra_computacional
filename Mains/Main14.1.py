from sage.all import *

import Structures.IntegerPolynomial as IntegerPolynomial
import Structures.Polynomial as Polynomial
import Structures.Integers as Integers
import Structures.IntegersModuleP
from Algorithms.MultivariateDiophant import univariate_diophant

Z = Integers.Integers()
R = IntegerPolynomial.IntegerPolynomial(Z, 'x')
S = IntegerPolynomial.IntegerPolynomial(R, 'y')

x = R.get_variable()
y = S.get_variable()

fl = [x**2 + 0*y, y**2, x**4*y, x+y+x*y+1]
al = [y, y - 1, y + 1, y - 2]
for f in fl:
    for g in al:
        print f,"centrada en", g, "vale:", S.p_adic_taylor_series(f, g)



