n = "1" * 101
while "1111" in n:
    n = n.replace("1111", "22", 1)
    n = n.replace("222", "1", 1)
print(n)