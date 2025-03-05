def F(n):
    lst = []
    n = str(n)
    lst.append(int(n[0]) + int(n[1]))
    lst.append(int(n[1]) + int(n[2]))
    lst.append(int(n[2]) + int(n[3]))
    lst.remove(min(lst))
    return str(min(lst)) + str(max(lst))

for i in range(1000, 10000):
    if F(i) == "1418":
        print(i)
        break