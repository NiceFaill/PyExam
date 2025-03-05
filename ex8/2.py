from itertools import permutations, product

sogl = ["П", "Л", "Н"]
glas = ["О", "И", "А"]

counter = 0
for x in permutations("ПОЛИНА", 6):
    s = "".join(x)
    if (s[0] in sogl and s[1] in glas and s[2] in sogl and s[3] in glas and s[4] in sogl and s[5] in glas) or \
    (s[0] in glas and s[1] in sogl and s[2] in glas and s[3] in sogl and s[4] in glas and s[5] in sogl):
        counter += 1
print(counter)