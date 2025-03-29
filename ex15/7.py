def F(a, x, y):
    return (y + 2*x != 48) or (a < x) or (x < y)

for a in range(500, -1, -1):
    if all(F(a, x, y)
           for x in range(0, 501)
           for y in range(0, 501)
           ):
        print(a)
        break