def f(x, y, p):
    if x + y >= 40 and p == 3: return True
    if x + y < 40 and p == 3: return False
    if x + y >= 40: return False
    
    if p % 2 == 1:
        return f(x + 1, y, p + 1) and f(x + 2, y, p + 1) and f(x + 3, y, p + 1) and f(x + 1, y + 1, p + 1) and f(x + 2, y + 2, p + 1) and f(x + 3, y + 3, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x + 2, y, p + 1) or f(x + 3, y, p + 1) or  f(x + 1, y + 1, p + 1) or f(x + 2, y + 2, p + 1) and f(x + 3, y + 3, p + 1)

for s in range(1, 133):
    if f(s, 1, 1):
        print(s)
