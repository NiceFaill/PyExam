with open("ex9/4.csv", "r") as f:
    cnt = 0
    for x in f:
        s = list(map(int, x.rstrip('\n').split(";")))
        p2 = [x for x in s if s.count(x) == 2]
        np = [x for x in s if s.count(x) == 1]
        if len(p2) == 2 and len(np) == 4:
            if sum(np)/len(np) <= sum(p2):
                cnt += 1
    print(cnt)