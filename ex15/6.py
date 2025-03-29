# (2x + 3y > 40) or ((x < A) and (y <= A))

def F(a, x, y):
    return (2*x +3*y > 40) or ((x < a) and (y <= a))

for a in range(0, 501):
    # isOk = True
    # for x in range(0, 501):
    #     for y in range(0, 501):
    #         if not(x, y, a):
    #             isOk = False
    #             break
    #     if not isOk:
    #         break
    # if isOk:
    #     print(a)
    #     break

    if all(F(x, y, a) 
           for x in range(0, 501)
           for y in range(0, 501)
           ):
        print(a)
        break
