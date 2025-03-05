with open("ex17/1.txt", "r") as f:
    lst = []
    counter = 0
    counter2 = 0
    for x in f:
        lst.append(x.rstrip("\n"))
    
    lst = list(map(int, lst))
    for i in range(len(lst) - 1):
        if (lst[i] % 3 == 0) or (lst[i + 1] % 3 == 0):
            counter += 1
            if lst[i] + lst[i + 1] > counter2:
                counter2 = lst[i] + lst[i + 1]
    print(counter, counter2)