lst = []
for i in range(16015, 48990):
    if ((i % 3 == 0) or (i % 11 == 0)) and \
        0 not in [i % 9, i % 12, i % 13]:
        lst.append(i)
print(len(lst), min(lst))
