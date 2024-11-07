def to4(n):
    res = ''
    while n >= 4:
        res = str(n % 4) + res
        n //= 4
    return int(str(n) + res)
a, b = [to4(int(i)) for i in input().split()]
d = str(a / b)
if len(d[d.index('.'):]) > 15:
    print('NO')
else:
    print(len(d[d.index('.') + 1:]))