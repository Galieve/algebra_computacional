from sage.all import *

import Structures.FiniteFields
import Structures.IntegersModuleP

print "Finite Field F83"

# la probabilidad de fallo es == 1/p, p = menor divisor del grupo multiplicativo.
# 83 - 1 == 82 => probabilidad = 1/2
# (83 - 1) // 2 = 41, primo => probabilidad = 1/41 << 1/2
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
    beta_ = K.mul(beta, beta) # beta_ = beta * beta
    for alpha in range(1, 83):
        alpha = alpha + K.zero()
        alpha_ = K.mul(alpha, alpha) # alpha_ = alpha * alpha

        # beta_ ** x == alpha_ => beta**(2*x) = alpha**2
        # o bien solucion = x, o bien solucion = x + 41 (41*2 = 82, gamma**82 == 1)

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