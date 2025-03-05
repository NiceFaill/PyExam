# Одна куча
# 1) +1
# 2) +2
# 3) *3

# 1 <= S <= 63
# T >= 64

from functools import lru_cache

@lru_cache
def F(x: int) -> str:
    if x >= 64:
        return ('F', 0)
    a1, b1 = F(x + 1)
    a2, b2 = F(x + 2)
    a3, b3 = F(x * 3)
    if a1 == 'W' and a2 == 'W' and a3 == 'W':
        a = 'F'
        b = 1 + max(b1, b2, b3)
    else:
        a = 'W'
        fails = []
        if a1 == 'F': fails.append(b1)
        if a2 == 'F': fails.append(b2)
        if a3 == 'F': fails.append(b3)
        b = 1 + min(fails)
    return (a, b)

for i in range(1, 64):
    print(i, F(i))

