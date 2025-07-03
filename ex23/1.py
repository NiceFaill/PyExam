def F(x, y):
    if x > y or x == 14: return 0
    if x == y: return 1
    return F(x + 1, y) + F(x * 2, y) + F(x**2, y)

print(F(3, 25))