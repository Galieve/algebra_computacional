from sage.all import *
from Structures.FiniteFields import FiniteFields

K = FiniteFields(5,2,'s');
s = K.get_variable();

for i in range(0,5):
    for j in range(0,5):
        for k in range(0,2):
            element = i + j*s**k;
            if element != 0:
                inv = K.inverse(element);
                print(inv, element, K.mul(inv,element));

