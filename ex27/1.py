# 5
# 150
# 200
# 300
# 250
# 180

# maximum:  300
# maximum2: 250
# x:        150

n = int(input())

maximum = -1
maximum2 = -1

for i in range(n):
    x = int(input())
    if x > maximum:
        maximum, maximum2 = x, maximum
    elif x > maximum2:
        maximum2 = x