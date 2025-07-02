from itertools import product, permutations
cnt = 0
for x in product("ABCDXYZ", repeat=4):
    s = "".join(x)
    if s[0] in "XYZ" and s[1] in "XYZ" and \
        s[2] in "ABCD" and s[3] in "ABCD":
            cnt += 1
print(cnt)