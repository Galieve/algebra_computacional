import Structures.Integers
import Structures.IntegersModuleP
import Structures.Polynomial

Z = Structures.Integers.Integers()
R = Structures.Polynomial.Polynomial(Z, 'y')
x = R.get_variable()
f = x**4 - 1
g = x**3 + 2 * x**2 - x - 2
h = x - 2
s = -2 + 0 * x
t = 2 * x**2 - 2 * x - 1
IMP = Structures.IntegersModuleP.IntegersModuleP(5)
RI = Structures.Polynomial.Polynomial(IMP, 'y')
x = RI.get_variable()
#hlist = RI.berlekamp(f, IMP.get_order())
hlist = [x - 1, x - 2, x + 2, x + 1]
# lmhl =  multifactor_hensel_lifting(5, f.list()[-1], hlist, RI, f, R, 4)
# print lmhl

#hasta aqui bien

Z = Structures.Integers.Integers()
R = Structures.Polynomial.Polynomial(Z, 'x')
x = R.get_variable()
f = x ** 3 - x + 1
g = x ** 2 - x - 1
j = f * g
i = x**2 + 2 * x + 1
k = x ** 8 + x ** 7 - x ** 6 + x ** 5 - x ** 3 - x ** 2 - x
l = 2*x**2 + 3*x

isqd = R.square_free_decomposition(i)
li = []
for i, m in isqd:
    li.append((R.hensel_lifting(i), m))
print li
print R.hensel_lifting(j)
print R.hensel_lifting(k)
print R.hensel_lifting(-j)
print R.hensel_lifting(-64 * j)
print R.hensel_lifting(l)