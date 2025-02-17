#decimal to binary
n = 186

while n > 0:
    print(n % 4, end="")
    n //= 4
print('')
