from sage.all import *
from Algorithms.MathAuxiliar import get_divisors
import Structures.FiniteFieldsWrapper
import Structures.FiniteFieldPolynomial

K = Structures.FiniteFieldsWrapper.FiniteFieldsWrapper(3, 5, 'a')
a = K.get_variable()
R = Structures.FiniteFieldPolynomial.FiniteFieldPolynomial(K, 'x')
x = R.get_variable()
f = x ** 3 - x + 1
g = x ** 2 - x - 1
h = x ** 2 + x - 1
j = f * g
i = h * g
k = x ** 8 + x ** 7 - x ** 6 + x ** 5 - x ** 3 - x ** 2 - x
# un polinomio p es libre de cuadrados si no existe ningun polinomio q "no constante" de manera que
# p = q**2 * r, con r un polinomio arbitrario
print("Square free decomposition:")
li = R.square_free_decomposition(i)
print(i, li)
lj = R.square_free_decomposition(j)
print(j, lj)
lk = R.square_free_decomposition(k)
print(k, lk)
print("")
print("Distinct degree decomposition:")
ddi = []
for p, m in li:
    ddi.append((R.distinct_degree_decomposition(p), m))
print "i: ", ddi

ddj = []
for p, m in lj:
    ddj.append((R.distinct_degree_decomposition(p), m))
print "j: ", ddj

ddk = []
for p, m in lk:
    ddk.append((R.distinct_degree_decomposition(p), m))
print "k: ", ddk
print("")
print("Equal degree decomposition:")

solk = []

for l, m in ddk:
    for poly in l:
        divisor = set(get_divisors(poly.degree()))
        for d in divisor:
            p = R.equal_degree_splitting(poly, d, 10)
            if p is not None:
                break
        if p is not None:
            for polynom in p:
                solk.append((polynom, m))
        else:
            solk.append((poly, m))

print "solucion =", solk
