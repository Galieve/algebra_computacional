from sage.all import *
import Structures.FiniteFields

print 'Finite Field F9'

K = Structures.FiniteFields.FiniteFields(3,2, 'a')
a = K.get_variable()
for i in range (0, 3):
    for j in range(0, 3):
        beta = K.add(j, K.mul(i, a))
        if K.multiplicative_order(beta) != K.get_order() - 1:
            continue
        for k in range (0, 3):
            for l in range(0, 3):
                alpha = K.add(l, K.mul(k, a))
                if alpha == K.zero():
                    continue
                lg = K.discrete_logarithm(alpha, beta)
                if lg is None:
                    print "No se puede calcular el logaritmo discreto de beta =", beta, "y alpha =", alpha
                else:
                    print beta, "**", lg, "=", alpha, "y al operar vemos que es:", \
                        K.repeated_squaring(beta, lg) == alpha