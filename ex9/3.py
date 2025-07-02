with open("ex9/3.csv", "r") as f:
    cnt = 0
    for x in f:
        s = list(map(int, x.rstrip("\n").split(";")))
        