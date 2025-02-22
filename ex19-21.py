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
        return 'F'
    a1 = F(x + 1)
    a2 = F(x + 2)
    a3 = F(x * 3)
    if a1 == "W" and a2 == "W" and a3 == "W":
        return "F"
    else:
        return "W"

for i in range(1, 64):
    print(i, F(i))


