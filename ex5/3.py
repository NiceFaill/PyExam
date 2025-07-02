def F(x):
    x = str(x)
    num1 = int(x[0]) + int(x[1])
    num2 = int(x[1]) + int(x[2])
    num3 = int(x[2]) + int(x[3])
    lst = [num1, num2, num3]
    lst.sort()
    lst.pop(0)
    return str(lst[0]) + str(lst[1])

for i in range(1000, 10000):
    if F(i) == "1517":
        print(i)