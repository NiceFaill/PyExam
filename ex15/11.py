def F(a, x):
    return a % 45 == 0 and 750 % x != 0 or a % x == 0 or 120 % x != 0

for a in range(1, 501):
    if all(F(a, x) for x in range(1, 501)):
        print(a)
        break