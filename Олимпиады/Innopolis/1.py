n = int(input())
M = [int(i) for i in input().split()]
mi = float('-inf')
res = 0
while True:
    for i in range(len(M) - 6):
        if min(M[i:i+7]) > mi:
            mi = min(M[i:i+7])
            ind = i
    if mi == 0:
        break
    for i in range(ind, ind + 7):
        M[i] -= 1
    res += 1
    mi = float('-inf')
print(res, sum(M))