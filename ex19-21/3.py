def F(k, x):
    if (x == 3 or x == 5) and k >= 29: return True
    if x == 5 and k < 29: return False
    if k >= 29: return False

    if x % 2 == 0:
        return F(k + 1, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 2, x + 1)
for i in range(1, 29):
    if F(i, 1):
        print(i)