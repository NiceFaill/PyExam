from itertools import product

cnt = 0
for x in product("ABCDEF", repeat=5):
    s = "".join(x)
    if s[0] != "F" and s[4] != "A":
        cnt += 1
print(cnt)