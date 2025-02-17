print("x y z w\tF=0")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((y <= w) == (x <= (not z)) and (x or w)):
                    print(x, y, z, w)
print('')
print("x y z w\tF=0")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((y <= w) == (x <= (not z)) and (x or w)):
                    print(x, y, z, w)