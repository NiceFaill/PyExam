with open("ex9/2.csv", "r") as f:
    counter = 0
    for x in f:
        x = x.rstrip("\n").split(";")
        minimum = int(min(x))
        maximum = int(max(x))
        x.remove(str(minimum))
        x.remove(str(maximum))
        if ((int(x[0]) + int(x[1]) + maximum) / 6 > minimum) and maximum * minimum > int(x[0]) * int(x[1]):
            counter += 1    
    print(counter)
    