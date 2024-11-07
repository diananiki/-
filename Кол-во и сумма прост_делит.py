x = int(input())
res1, res2 =0, 0
for i in range(1, int(x**0.5)+1):
    if x % i == 0:
        if i**2 == x:
            res1 += 1
            res2 += i
        else:
            res1 += 2
            res2 = res2 + i + x // i
print(res1, res2)