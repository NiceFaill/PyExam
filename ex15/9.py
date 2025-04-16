def F(a, x, y):
    return (x >= 6 or x**2 < a) and (y**2 > a or y <= 6)

k = 0
for a in range(0, 501):
    if all(F(a, x, y)
           for x in range(0, 501)
           for y in range(0, 501)
           ):
        k += 1
        print(a, end=" ")
    
print()
print(k)