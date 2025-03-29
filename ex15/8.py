def F(a, x, y):
    return (y + 2 * x != 48) or (a < x) or (x < y)

for a in range(0, 501):
    if not all(F(a, x, y)
               for x in range(0, 501)
               for y in range(0, 501)
               ):
        print(a)
        break