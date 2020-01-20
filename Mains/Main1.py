from Structures.Integers import Integers
from Structures.GaussianIntegers import GaussianIntegers
from Structures.FiniteFieldsWrapper import FiniteFieldsWrapper
from Structures.Polynomial import Polynomial

Z = Integers()

print "El mcd de 33 y 0 es:", Z.euclides(33,0)
print ""

print "El mcd de 72 y -60 es:", Z.euclides(72,-60)
print ""

g, s, t = Z.extended_euclides(72,-60)
print "El mcd de 72 y -60 es:", g, "y", s, "* 72 +", t, "* (-60) ==", Z.add(Z.mul(s, 72), Z.mul(t, -60))
print ""


g, s, t = Z.extended_euclides(15, -30)
print "El mcd de 15 y -30 es:", g, "y", s, "* 15 +", t, "* (-30) ==", Z.add(Z.mul(s, 15), Z.mul(t, -30))
print ""

G = GaussianIntegers()
print "El mcd de 5 + 3 * i y 2 + (-8) * i es:", G.euclides((5,3),(2,-8))
print ""

g, s, t = G.extended_euclides((5,3),(2,-8))
print "El mcd de 5 + 3 * i y 2 + (-8) * i es:", g, "y", s, "*  (5 + 3 * i) +", t, "* (2 + (-8) * i) ==", G.add(G.mul(s, (5,3)), G.mul(t, (2,-8)))
print ""

F = FiniteFieldsWrapper(3, 1, 'a')
a = F.get_variable()
R = Polynomial(F,'t')
t = R.get_variable()
f = 4*t**2 + 7*t
g = 2*t**2 + t
h, i, j = R.extended_euclides(f,g)
print "mcd(", f, ",", g, ") ==", h
print "Ademas: (", f, ") * (", i, ") + (", g, ") * (", j, ") ==", R.add(R.mul(i, f), R.mul(j, g))
print ""


F = FiniteFieldsWrapper(5,2,'a')
a = F.get_variable()
R = Polynomial(F,'t')
t = R.get_variable()
f = t**2 + t + 32
g = 3*(a**3+2)*t**4 - t**3 + t + 1
h, i, j = R.extended_euclides(f,g)
print "mcd(", f, ",", g, ") ==", h
print "Ademas: (", f, ") * (", i, ") + (", g, ") * (", j, ") 0==", R.add(R.mul(i, f), R.mul(j, g))

