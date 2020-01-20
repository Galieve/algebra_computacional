import Structures.Integers
import Structures.GaussianIntegers

i = Structures.Integers.Integers()
m_list = [8,5,11]
u_list = [1,4,4]
solution = i.chinese_reminder(m_list, u_list)
for u, m in zip(u_list, m_list):
    print solution, " modulo ", m, " es igual a: ", i.mod(solution, m)

print ""


g = Structures.GaussianIntegers.GaussianIntegers()
m_list = [(11,0), (13,-1)]
u_list = [(2,3),(7,5)]
solution = g.chinese_reminder(m_list, u_list)
for u, m in zip(u_list, m_list):
    print solution, " modulo ", m, " es igual a: ", g.mod(solution, m)
assert(g.mod((7,5),(13,-1)) == g.mod((-6,6),(13,-1)))

