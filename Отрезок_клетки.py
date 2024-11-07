def NOD(a, b):
    while a > 0:
        a, b = max(a, b), min(a, b)
        a = a % b
    return b
x1, y1, x2, y2 = [int(i) for i in input().split()]
a, b = max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2)
if a==0 or b==0:
    print(0)
    exit()
x = max(1, NOD(a, b))
print((a//x + b//x - 1)*x)