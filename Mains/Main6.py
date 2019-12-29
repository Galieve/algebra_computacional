from sage.all import *
from Structures.FiniteFields import FiniteFields

K = FiniteFields(7, 1, 'a')
a = K.get_variable()
for beta in range(5,7):
    for alpha in range(5, 7):
        #alpha = alpha + 0*a
        beta = beta + 0*a
        lg = K.discrete_logarithm(alpha, beta)
        if lg is None:
            print "No se puede calcular el logaritmo discrteto de beta =", beta, "y alpha =", alpha
        else:
            beta = int(beta)
            print beta, "**", lg, "=", alpha, (beta**lg)%7 == alpha
