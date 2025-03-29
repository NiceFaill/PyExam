def F(x, a):
    return x & 28 == 0 or x & 45 == 0 or x & 17 != 0 or x & a != 0

for a in range(1, 501):
    if all(F(x, a) for x in range(1, 501)):
        print(a)
        break