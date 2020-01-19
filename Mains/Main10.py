import Structures.Integers

Z = Structures.Integers.Integers()

for i in range(2, 100):
    if Z.aks(i):
        print i, "es primo"
    else:
        print i, "no es primo"


