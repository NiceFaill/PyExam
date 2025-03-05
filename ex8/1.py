# -*- coding: cp1251 -*-
#11 exsercice
from itertools import permutations, product

i = 0
for x in product("ЕКМОПРТЬЮ", repeat=5):
    i += 1
    s = "".join(x)
    if (i % 2 != 0) and (s[0] != 'Ь') and (s.count('К') == 2):
        s0 = s
        i0 = i
print(i0, s0)