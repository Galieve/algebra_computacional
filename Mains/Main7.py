from sage.all import *
from Algorithms.MathAuxiliar import get_divisors
import Structures.FiniteFieldsWrapper
import Structures.FiniteFieldPolynomial

def full_descomposition_distinct_degree(ddk):
    solk = []

    for l, m in ddk:
        for poly in l:
            divisor = get_divisors(poly.degree())
            divisor.sort()
            for d in divisor:
                p = R.equal_degree_splitting(poly, d, 100)
                if p is not None:
                    break
            if p is not None:
                for polynom in p:
                    solk.append((polynom, m))
            else:
                solk.append((poly, m))
    return solk


K = Structures.FiniteFieldsWrapper.FiniteFieldsWrapper(3, 5, 'a')
a = K.get_variable()
R = Structures.FiniteFieldPolynomial.FiniteFieldPolynomial(K, 'x')
x = R.get_variable()
f = x ** 3 - x + 1
g = x ** 2 - x - 1
h = x ** 2 + x - 1
j = f * g
i = h * g * g
k = x ** 8 + x ** 7 - x ** 6 + x ** 5 - x ** 3 - x ** 2 - x
l = (x**2 + 1) * (x**2 + 2 *a + 2) * (2*a*x**2 + x + a + 1)

# un polinomio p es libre de cuadrados si no existe ningun polinomio q "no constante" de manera que
# p = q**2 * r, con r un polinomio arbitrario
print("Square free decomposition:")
li = R.square_free_decomposition(i)
print "i:",i, "se descompone como:", li
lj = R.square_free_decomposition(j)
print "j:", j, "se descompone como:",  lj
lk = R.square_free_decomposition(k)
print "k:", k, "se descompone como:",  lk
ll = R.square_free_decomposition(l)
print "l:", l, "se descompone como:",  ll
print("")
print("Distinct degree decomposition:")
ddi = []
for p, m in li:
    ddi.append((R.distinct_degree_decomposition(p), m))
print "i:", ddi

ddj = []
for p, m in lj:
    ddj.append((R.distinct_degree_decomposition(p), m))
print "j:", ddj

ddk = []
for p, m in lk:
    ddk.append((R.distinct_degree_decomposition(p), m))
print "k:", ddk

ddl = []
for p, m in ll:
    ddl.append((R.distinct_degree_decomposition(p), m))
print "l:", ddl
print("")
print("Equal degree decomposition:")


solk = full_descomposition_distinct_degree(ddk)
print "descomposicion de k:", solk
soll = full_descomposition_distinct_degree(ddl)
print "descomposicion de l:", soll
