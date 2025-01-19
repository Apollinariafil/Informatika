from sys import setrecursionlimit

# Увеличение глубины рекурсии до 3000
setrecursionlimit(3000)


def F(n):
    if n > 3456:
        return n + 1
    if n <= 3456 and n % 3 == 0:
        return F(n + 1) + F(n + 2)
    if n <= 3456 and n % 3 != 0:
        return F(n + (n % 3)) + 2


print(F(12)-F(17))


# F = [1] * 5000
# for n in range(len(F)):
#     # if n <= 1:
#     #     F[n] = 1
#     if n > 3456 and (n > 1):
#         F[n] = n + 1
#     if n <= 3456 and ((n % 3) == 0) and (n > 1):
#         F[n] = F[n - 1] + F[n - 2]
#     if n <= 3456 and ((n % 3) != 0) and (n > 1):
#         F[n] = F[n - (n % 3)] + 2
# print(F[12])


# for n in range(len(F)):
#     if n >= 2025:
#         F[n] = n
#     if n < 2025:
#         F[n] = n + 3 + F[n + 3]
# print(F[23])
