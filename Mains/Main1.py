from Structures.Integers import Integers

from Structures.GaussianIntegers import GaussianIntegers

from Structures.FiniteFieldsWrapper import FiniteFieldsWrapper

from Structures.Polynomial import Polynomial

i = Integers()

print i.euclides(72,-60)
print i.euclides(33,0)
print i.extended_euclides(72,-60)
print i.unit_normal(-60)

g = GaussianIntegers()
print g.euclides((5,3),(2,-8))
print g.extended_euclides((5,3),(2,-8))

F = FiniteFieldsWrapper(3, 1, 'a')
a = F.get_variable()
R = Polynomial(F,'t')
t = R.get_variable()
f = 4*t**2+7*t
g = 2*t**2+t
print(R.extended_euclides(f,g))
#print(R.extended_euclides(f,0))


F = FiniteFieldsWrapper(5,2,'a')
a = F.get_variable()
R = Polynomial(F,'t')
t = R.get_variable()
f = t**2+t+32
g = 3*(a**3+2)*t**4-t**3+t+1
print(R.extended_euclides(f,g))

print (i.euclides(15,-30))

