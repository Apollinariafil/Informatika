from itertools import *

#3
#4  

def number(a, b, c, d):
    return int(str(a)+str(b)+str(c)+str(d))

# 29106
for a, b, c, d in product([0,1,2,3,4,5,6,7,8,9], repeat=4):
    if a<b<c<d:
        s = (a, b, c, d)
        print()
        print()
        res = 0
        for p in permutations("bcd"):
            arg = ['a']
            arg.extend(p)
            kwargs = dict(zip(arg, s))
            # print(kwargs)
            print(number(**kwargs))
            res += number(**kwargs)

        if res == 29106:
            print()
            print()
            print(s)
            break
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