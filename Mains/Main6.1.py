from sage.all import *

import Structures.FiniteFields
import Structures.IntegersModuleP

print "Finite Field F83"
K = Structures.FiniteFields.FiniteFields(83, 1, 'a')
a = K.get_variable()
q = (83 - 1)//2
IMP = Structures.IntegersModuleP.IntegersModuleP(83)
for beta in range(2,83):
    beta = beta + K.zero()
    # test beta == generador del grupo multiplicativo.
    if K.multiplicative_order(beta) != K.get_order() - 1:
        continue
    beta = beta + K.zero()
    beta_ = K.mul(beta, beta)
    for alpha in range(1, 83):
        alpha = alpha + K.zero()
        alpha_ = K.mul(alpha, alpha)

        lg = K.discrete_logarithm_n(alpha_, beta_, q)
        if lg is None:
            print "No se puede calcular el logaritmo discreto de beta =", beta, "y alpha =", alpha
        else:
            # hay dos "posibles" soluciones: lg y lg + q
            if K.repeated_squaring(beta, lg) != alpha:
                lg = lg + q
            print beta, "**", lg, "=", alpha, "y al operar vemos que es:",\
                K.repeated_squaring(beta, lg) == alpha

print ""

print "Finite Field F5"
K = Structures.FiniteFields.FiniteFields(5, 1, 'a')
a = K.get_variable()
q = (83 - 1)//2
IMP = Structures.IntegersModuleP.IntegersModuleP(5)
for beta in range(2,5):
    beta = beta + K.zero()
    # test beta == generador del grupo multiplicativo.
    if K.multiplicative_order(beta) != K.get_order() - 1:
        continue
    beta = beta + K.zero()
    for alpha in range(1, 5):
        alpha = alpha + K.zero()

        lg = K.discrete_logarithm(alpha, beta)
        if lg is None:
            print "No se puede calcular el logaritmo discreto de beta =", beta, "y alpha =", alpha
        else:
            # hay dos "posibles" soluciones: lg y lg + q
            if K.repeated_squaring(beta, lg) != alpha:
                lg = lg + q
            print beta, "**", lg, "=", alpha, "y al operar vemos que es:",\
                K.repeated_squaring(beta, lg) == alpha