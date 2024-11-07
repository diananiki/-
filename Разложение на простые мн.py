nn = int(input())
res, n = [], nn
i = 2
while i < nn**0.5 + 1:
    c = 0
    while n % i == 0:
        c += 1
        n //= i
    if c > 0:
        res += [str(i) + ('^' + str(c) if c > 1 else '')]
    i += 1
if n > 1:
    res += [str(n)]
print(*res, sep = '*')