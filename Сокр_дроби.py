def NOD(a, b):
    while a > 0:
        a, b = max(a, b), min(a, b)
        a = a % b
    return b
a, b = [int(i) for i in input().split()]
n = NOD(abs(a), b)
print(a//n, b//n)