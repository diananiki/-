def NOD(a, b):
    while a > 0:
        a, b = max(a, b), min(a, b)
        a = a % b
    return b
a, b = [int(i) for i in input().split()]
print(a*b//NOD(a, b))