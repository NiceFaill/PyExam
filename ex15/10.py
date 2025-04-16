def isTriangle(x, y, z):
    return x + y > z and x + z > y and y + z > x

def F(a, x):
    return not((isTriangle(x, 11, 16) == (max(x, 5) <= 10)) and isTriangle(4, a, x))

for a in range(500, 0, -1):
    if all(F(a, x) for x in range(0, 501)):
        print(a)
        break