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
