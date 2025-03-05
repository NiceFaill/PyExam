# import sys
# sys.setrecursionlimit(100000)

# def F(n):
#     if n <= 2:
#         return n
#     if n > 2:
#         return n * F(n - 1)

# print(F(2025) / F(2022))

# A = 2026 * [0]
# A[1] = 1
# A[2] = 2
# for n in range(3, 2026):
#     A[n] = n * A[n - 1]
# print(A[2025] / A[2022])

# lst = []
# def F(n):
#     lst.append(n)
#     if n >= 3:
#         F(n - 1)
#         lst.append(3 * n + 2)
#         F(n // 2)
#         lst.append(2 * n + 6)
#     lst.append(2 * n)
# F(5)
# print(sum(lst))

# A = 51 * [0]
# A[1] = 3
# A[2] = 6

# for n in range(3, 51):
#     A[n] = n + A[n - 1] + (3 * n + 2) + A[n // 2] + (2 * n + 6) + (2 * n)
# print(A[50])

# Чему равна сумма чисел, которые напечатаются на экране при вызове F(2) ?

#1st way!!!!

# summ = 0
# def F(n):
#     global summ
#     summ += 4 * n
#     if n <= 5:
#         F(n + 1)
#         summ += 3 * n + 2
#         F(2 * n + 1)
#         summ += 2 * n - 4
#     summ += n
# F(2)
# print(summ)

# A = 20 * [0]

# for n in range(19, 5, -1):
#     A[n] = 4 * n + n

# for n in range(5, 1, -1):
#     A[n] = 4 * n + A[n + 1] + (3 * n + 2) + A[2 * n + 1] + (2 * n - 4) + n

# print(A[2])
