# (ДЕЛ(n, m))
# (A < 50) and (not(ДЕЛ(x, A)) <= (ДЕЛ(x, 10)) <= not(ДЕЛ(x, 18))))

def F(x, a):
    return x % a == 0 or x % 10 != 0 or x % 18 != 0

for a in range(49, 0, -1):
    if all(F(x, a) for x in range(1, 501)):
        print(a)
        break        