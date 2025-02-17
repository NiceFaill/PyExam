# s = "B" * 68
# while ("AAA" in s) or ("BBB" in s):
#     if("AAA" in s):
#         s = s.replace("AAA", "B", 1)
#     else:
#         s = s.replace("BBB", "A", 1)
# print(s)

# s = "1" + "8" * 80
# while "18" in s or "288" in s or "3888" in s:
#     if("18" in s):
#         s = s.replace("18", "2", 1)
#     elif("288" in s):
#         s = s.replace("288", "3", 1)
#     else:
#         s = s.replace("3888", "1", 1)
# print(s)

# s = "2" * 3 + "5" * 18
# while ("222" in s) or ("888" in s):
#     while ("555" in s):
#         s = s.replace("555", "8", 1)
#     if ("222" in s):
#         s = s.replace("222", "8", 1)
#     else:
#         s = s.replace("888", "2", 1)
# print(s)

# s = ">" + 10 * "1" + 20 * "2" + 30 * "3"
# while(">1" in s) or (">2" in s) or (">3" in s):
#     if(">1" in s):
#         s = s.replace(">1", "22>", 1)
#     if(">2" in s):
#         s = s.replace(">2", "2>")
#     if(">3" in s):
#         s = s.replace(">3", "1>")

# s = s[:-1]
# s = map(int, list(s))
# print(sum(s))

# def isPrime(x):
#     if x <= 1:
#         return False
#     r = int(x ** 0.5)
#     for d in range(2, r + 1):
#         if x % d == 0:
#             return False
#     return True
# lst = []
# for i in range(0, 101):
#     s = ">" + 39 * "0" + i * "1" + 39 * "2"
#     while (">1" in s) or (">2" in s ) or (">0" in s):
#         if ">1" in s:
#             s.replace(">1", "22>", 1)
#         if ">2" in s:
#             s.replace(">2", "2>", 1)
#         if ">0" in s:
#             s.replace(">0", "1>", 1)
#     s = s[:-1]
#     summa = sum(map(int, list(s)))
#     if(isPrime(summa)):
#         lst.append(summa)
# print(lst)


