# ДЕЛ(A, 45) or (ДЕЛ(750, x)) <= (not(ДЕЛ(A, x)) <= not(ДЕЛ(120, x))))

def F(x, a):
    return 750 % x != 0 or a % x == 0 or 120 % x != 0

for a in range(45, 10001, 45):
    if all(F(x, a) for x in range(1, 501)):
        print(a)
        break