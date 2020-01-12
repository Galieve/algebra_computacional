from sage.all import *
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
print("Berlekamp:")
soli = []
for i, m in li:
    soli.append((R.berlekamp(i, 10), m))
print "solucion i =", soli
solj = []
for j, m in lj:
    solj.append((R.berlekamp(j, 10), m))
print "solucion j =", solj
solk = R.berlekamp(k, 10)
solk = []
for k, m in lk:
    solk.append((R.berlekamp(k, 10), m))
print "solucion j =", solk
