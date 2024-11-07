def From2(a):
    res = 0
    for i in range(len(a)):
        if a[i] == '1':
            res += 2 ** (len(a) - 1 - i)
    return res

def To2(a):
    res = ''
    while a > 0:
        res = str(a % 2) + res
        a //= 2
    return res

a, b = [int(i) for i in input().split()]
if b % 2 == 0:
    b -= 1
k1 = 0

n = To2(b)
while True:
    k = n.count('1')
    if k > k1:
        k1 = k
        res = b
    n = n[::-1]
    if '0' not in n:
        print(res)
        exit()
    i0 = n.index('0')
    if '1' not in n[i0+1:]:
        print(res)
        exit()
    i1 = n.index('1', i0+1)
    n = n[:i0] + '1' * (i1-i0) + '0' + n[i1+1:]
    n = n[::-1]
    b = From2(n)
    if b < a:
        print(res)
        exit()