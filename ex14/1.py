#ex 1
# num = 4 * 125 ** 6 - 25 ** 4 + 9
# lst = []
# while num > 0:
#     d = num % 5
#     lst.append(d)
#     num //=5
# print(lst.count(4))

#ex 2
# a = 729 ** 11 - 2 * 243 ** 12 + 81 ** 13
# for b in range(999, 99, -1): #b = 999, 998, 997, ..., 100
#     n = a - b
#     k = 0
#     while n > 0:
#         d = n % 3
#         if d == 2:
#             k += 1
#         n //= 3
#     if k == 55:
#         print(b)
#         break

#ex 3
# s = "0123456789ABCDEFGHI"
# for x in s:
#     s1 = "98897" + x + "21"
#     s2 = "2" + x + "923"
#     a = int(s1, 19)
#     b = int(s2, 19)
#     c = a + b
#     if c % 18 == 0:
#         print(x, c // 18)

for x in "0123456789ABCDEFGHI":
    for y in "0123456789ABCD":
        s1 = "98897" + x + "21"
        s2 = "2" + y + "923"
        a = int(s1, 19)
        b = int(s2, 14)
        c = a + b
        if c % 18 == 0:
            print(x, c // 18)