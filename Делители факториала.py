M = [[0]*46 for i in range(46)]
for nn in range(2, 46):
    res, n = [], nn
    i = 2
    while i < nn ** 0.5 + 1:
        c = 0
        while n % i == 0:
            c += 1
            n //= i
        if c > 0:
            M[nn][i] = c
        i += 1
    if n > 1:
        M[nn][n] = 1
n = int(input())
res = []
c = 0
for i in range(n+1):
    for j in range(n+1):
        if M[j][i] > 0:
            c += M[j][i]
    if c > 0:
        res += [[i, c]]
        c = 0
RES = 1
for i in res:
    RES *= i[1]+1
print(RES)