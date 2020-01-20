from sage.all import *
from Structures.FiniteFields import FiniteFields

K = FiniteFields(5, 2, 's');
s = K.get_variable();

calculated = set()
for i in range(0, 5):
    for j in range(0, 5):
        for k in range(0, 2):
            element = i + j * s ** k;
            if element != 0 and element not in calculated:
                calculated.add(element)
                inv = K.inverse(element);
                print "(", element, ") * (", inv, ") ==", K.mul(inv, element)
