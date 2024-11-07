n, k = [int(i) for i in input().split()]
if k == 0:
    print(n)
    exit()
i2, i5 = 0, 0
while n % 2 == 0:
    i2 += 1
    n //= 2
while n % 5 == 0:
    i5 += 1
    n //= 5
i2, i5 = max(i2, k), max(i5, k)
print(n * 2 ** i2 * 5 ** i5)