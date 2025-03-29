# m & n
# (x & 29 != 0) <= (not(x & 17 != 0)) <= (x & A != 0))

# not(x & 29 != 0) or (x & 17 != 0 or (x & A != 0))

def F(x, a):
    return x & 29 == 0 or x & 17 != 0 or x & a != 0

for a in range(1, 501):
    if all(F(x, a) for x in range(1, 510)):
        print(a)
        break