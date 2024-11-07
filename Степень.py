#N**N делится на а
nn = int(input())
if nn == 1:
    print(1)
    exit()
res, n = [], nn
i = 2
while i < nn**0.5 + 1:
    c = 0
    while n % i == 0:
        c += 1
        n //= i
    if c > 0:
        res += [i]
    i += 1
if n > 1:
    res += [n]
Res = 1
for i in res:
    Res *= i
if Res >= 29:
    print(Res)
    exit()
for i in range(1, 30):
    if (Res*i)**(Res*i) % nn == 0:
        print(Res*i)
        exit()