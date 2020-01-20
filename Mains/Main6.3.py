from sage.all import *
import Structures.FiniteFieldsWrapper
import Structures.Polynomial
import Structures.QuotientFiniteField


# hecho ad hoc para k = 2
def generate_elements(p, K):
    a = K.get_variable()
    l = []
    for i in range(0, p):
        for j in range(0, p):
            l.append(K.add(j, K.mul(i, a)))
    return l


# hecho ad hoc para degree de f = 2
def generate_polynomials(p, K, R):
    x = R.get_variable()
    l = []
    l_ = generate_elements(p, K)
    for i in l_:
        for j in l_:
            l.append(R.add(j, R.mul(i, x)))
    return l


print 'Quotient Finite Field F9[X]/(x**2+x+2)'
K = Structures.FiniteFieldsWrapper.FiniteFieldsWrapper(3, 2, 'a')
a = K.get_variable()
R = Structures.Polynomial.Polynomial(K, 'x')
x = R.get_variable()

f = x ** 2 + 2*a*x + 2
QF = Structures.QuotientFiniteField.QuotientFiniteField(R, f)

list_ = generate_polynomials(3, K, R)

for beta in list_:
    if QF.multiplicative_order(beta) != QF.get_order() - 1:
        continue
    for alpha in list_:
        if alpha == QF.zero():
            continue
        lg = QF.discrete_logarithm(alpha, beta)
        if lg is None:
            print "No se puede calcular el logaritmo discreto de beta =", beta, "y alpha =", alpha
        else:
            print beta, "**", lg, "=", alpha, "y al operar vemos que es:", \
                QF.repeated_squaring(beta, lg) == alpha
