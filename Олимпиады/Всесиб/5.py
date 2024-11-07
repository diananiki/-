import copy
import queue
f = open('input.txt')
Q = queue.Queue()
n, m, bon = [int(i) for i in f.readline().split()]
sx, sy = [int(i) - 1 for i in f.readline().split()]
M, B = [0] * n, []
for i in range(n):
    M[i] = list(f.readline())[:-1]
for i in range(bon):
    B += [[int(q)-1 for q in f.readline().split()]]
    B[i][2] += 1
for i in range(n):
    for j in range(m):
        if M[i][j] == '.':
            for z1 in range(2):
                for z2 in range(2):
                    x1, y1 = i + z1 - z2, j + z1 + z2 - 1
                    if not(0 <= x1 < n and 0 <= y1 < m):
                        continue
                    if M[x1][y1] != 'X':
                        if M[i][j] == '.':
                            M[i][j] = 1
                        else:
                            M[i][j] += 1
        if M[i][j] == '.':
            M[i][j] = 0
RES = 0
res = 0
Q.put((sx, sy, M, B, res))
while Q.qsize() > 0:
    x, y, M, B, res = Q.get()
    if M[x][y] == 0:
        continue
    F = False
    for w in B:
        if w[2] > 0:
            F = True
            break
    if not F:
        continue
    for a in range(len(B)):
        if B[a][0] == x and B[a][1] == y:
            res += B[a][2]
            RES = max(RES, res)
            del B[a]
            break
    M[x][y] -= 1
    for z1 in range(2):
        for z2 in range(2):
            x1, y1 = x + z1 - z2, y + z1 + z2 - 1
            if not (0 <= x1 < n and 0 <= y1 < m):
                continue
            if M[x1][y1] != 'X':
                Q.put((x1, y1, copy.deepcopy(M), copy.deepcopy(B), res))
print(RES)