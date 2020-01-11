import Structures.Integers
Z = Structures.Integers.Integers()

for i in range(2, 100):
    if Z.miller_rabin(i, 10):
        print i, "es primo"
    else:
        print i, "no es primo"