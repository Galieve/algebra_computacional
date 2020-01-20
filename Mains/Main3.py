from sage.all import *

from Structures.Polynomial import Polynomial
from Structures.Integers import Integers

i = Integers()
R = Polynomial(i, 's')
s = R.get_variable()
f = 48 * s ** 3 - 84 * s ** 2 + 42 * s - 36
g = -4 * s ** 3 - 10 * s ** 2 + 44 * s - 30
h = -30 * s

print "mcd(", f, ",", g, ") ==", R.gcd(f, g), "\n"

R = Polynomial(i, 'y')
Q = Polynomial(R, 'x')
y = R.get_variable()
x = Q.get_variable()
f = -30 * x ** 3 * y + 90 * x ** 2 * y ** 2 + 15 * x ** 2 - 60 * x * y + 45 * y ** 2
g = -1 * (100 * x ** 2 * y - 140 * x ** 2 - 250 * x * y ** 2 + 350 * x * y - 150 * y ** 3 + 210 * y ** 2)

print "mcd(", f, ",", g, ") ==", Q.gcd(f, g)
