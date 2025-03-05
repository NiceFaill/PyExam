def func(n):
    s = bin(n)[2:]
    if (int(s) % 2 == 0): s += "01"
    else: s += "10"
    return int(s, 2)

lst = []
for i in range(2, 1000000):
    r = func(i)
    if(r < 92):
        lst.append(r)
print(min(lst))

