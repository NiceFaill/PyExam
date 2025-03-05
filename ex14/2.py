num = 36 ** 7 + 6 ** 19 - 18
numm = ""
while num > 0:
    numm += str(num % 6)
    num //= 6
print(numm.count("5"))