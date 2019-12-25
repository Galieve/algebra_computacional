from sage.all import *
from Structures.FiniteFields import FiniteFields

#IMP = IntegersModuleP(7)
#print(IMP.inverse(5))

K = FiniteFields(5,2,'s');
s = K.get_variable();
print("hola caracola");
#print((s+1)*(4*s+4))


for i in range(0,5):
    for j in range(0,5):
        for k in range(0,2):
            element = i + j*s**k;
            if element != 0:
                inv = K.inverse(element);
                print(inv, element, K.mul(inv,element));

