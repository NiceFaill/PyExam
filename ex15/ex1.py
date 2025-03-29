# (ДЕЛ(n, m))
# (ДЕЛ(x, 2) <= not(ДЕЛ(x, 3))) or (x + A >= 100)

def F(x, a):
    return x % 2 != 0 or x % 3 != 0 or x + a >= 100

for a in range(1, 501):

    # isOk = True
    # for x in range(1, 501):
    #     if not(F(x, a)):
    #         isOk = False
    #         break
    # if (isOk):
    #     print(a)
    #     break
    
    if all(F(x, a) for x in range(1, 501)):
        print(a)
        break