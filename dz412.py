from itertools import*
def u(a, b, c, d):
    return (c and (a or d) and (d <= b))

for q, w, e, r, t, y in product([0, 1], repeat = 6):
    table = ((q, e, t, 0, 1),
             (w, 1, 0, y, 1),
             (0, r, 1, 0, 1))
    if len(table) == len(set(table)):
        for p in permutations("abcd"):
            if all(u(**dict(zip(p, r)))== r[-1] for r in table):
                print(*p)