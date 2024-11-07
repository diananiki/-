d, n = [int(i) for i in input().split()]
M = []
for i in range(n):
    M += [int(input())]
if sum(M) < d:
    print('NO')
    exit()
M.sort()
M = M[::-1]
while M[0] > d:
    del M[0]
R = [[M[0]]]
minn = float('+inf')
for i in range(1, len(M)):
    for j in range(len(R)):
        R += [R[j] + [M[i]]]
        if sum(R[-1]) == d:
            if len(R[-1]) < minn:
                minn = len(R[-1])
                ind = len(R) - 1
    R += [[M[i]]]
if minn < float('+inf'):
    print(minn)
    print(*R[ind], sep = '\n')
else:
    print('NO')