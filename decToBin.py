#decimal to binary

def toFour(n):
    binNum = ""
    while n > 0:
        binNum = str(n % 4) + binNum
        n //= 4
    return binNum

print(toFour(169))
