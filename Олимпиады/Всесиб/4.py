def NOD(a, b):
    while a > 0:
        a, b = max(a, b), min(a, b)
        a = a % b
    return b
n, a, b = [int(i) for i in input().split()]
mi = max(n/3, (n-b)/2)
ma = min(n/2, (n+a)/2)
n = int(ma) - int(mi)
if mi % 1 > 0:
    n += 1
m = (a+1)*(b+1)
if n == m:
    print(1)
elif n == 0:
    print(0)
else:
    nod = NOD(m, n)
    print(n//nod, '/', m//nod, sep="")