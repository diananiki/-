f = open('input.txt')
n = int(f.readline())
M = [[0] * n for i in range(n)]
for i in range(n-1):
    x, y = [int(i)-1 for i in f.readline().split()]
    M[x][y], M[y][x] = 1, 1
g = 0
for i in range(n):
    if sum(M[i]) > g:
        g = sum(M[i])
        r = i
O = []
v = [0] * n
for i in range(n):
    if M[r][i] == 1:
        O.append([str(i), 0])
while len(O) > 0:
    for i in range(n):
        if M[int(O[0][0][-1])][i] == 1 and i != r and (len(O[0][0]) == 1 or len(O[0][0]) > 1 and i != int(O[0][0][-2])):
            O += [[O[0][0] + str(i), O[0][1] + 1]]
        if i == n-1:
            v[int(O[0][0][0])] = O[0][1]
            del O[0]
res = 0
for i in range(len(v)):
    if M[r][i] == 1:
        res += (v[i] + 1)**2
print(res, r+1)