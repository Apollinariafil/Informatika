from itertools import *


def number(a, b, c, d):
    return int(str(a)+str(b)+str(c)+str(d))


def number3(a, b, c):
    return int(str(a)+str(b)+str(c))


for a, b, c, d in product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=4):
    n1 = number3(a, b, c)
    n1 = 3*n1 + a
    n2 = number3(b, c, d)
    if n1 == n2:
        print((a, b, c, d))
        print(f'n1 = {n1} n2 = {n2}')
   # res = 0
    # for p in permutations("bcd"):
    #     arg = ['a']
    #     arg.extend(p)
    #     kwargs = dict(zip(arg, s))
    #     # print(kwargs)
    #     print(number(**kwargs))
    #     res += number(**kwargs)

    # if res == 29106:
    #     print()
    #     print()
    #     print(s)
    #     break


# 29106
# for a, b, c, d in product([0,1,2,3,4,5,6,7,8,9], repeat=4):
#     if a<b<c<d:
#         s = (a, b, c, d)
#         print()
#         print()
#         res = 0
#         for p in permutations("bcd"):
#             arg = ['a']
#             arg.extend(p)
#             kwargs = dict(zip(arg, s))
#             # print(kwargs)
#             print(number(**kwargs))
#             res += number(**kwargs)

#         if res == 29106:
#             print()
#             print()
#             print(s)
#             break
    #    s= u(**dict(zip(p, list)))
        # print(list(p))
        # if all(u(**dict(zip(p, r))) == r[-1] for r in table):
        #     print(*p)

    # table = ((q, e, t, 0, 1),
    #          (w, 1, 0, y, 1),
    #          (0, r, 1, 0, 1))
    # if len(table) == len(set(table)):
    #     for p in permutations("abcd"):
    #         if all(u(**dict(zip(p, r))) == r[-1] for r in table):
    #             print(*p)
