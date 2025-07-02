def F(n):
    s = bin(n)[2:]
    if int(s) % 2 == 0:
        s += "00"
    else:
        s = "11" + s
    return int(s, 2)

maxx = 0
for i in range(1000):
    if F(i) < 94 and F(i) > maxx:
        maxx = i
        
print(maxx)