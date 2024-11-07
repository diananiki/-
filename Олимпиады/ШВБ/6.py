def H(x, y, M, n):
    if n == 'W':
        n = 'B'
    else:
        n = 'W'
    if x + 2 < 8 and y + 2 < 8 and M[x+1][y+1] == n and M[x+2][y+2] == '.':
        M[x+1][y+1] = '.'
        return [True, x+2, y+2, M]
    elif x - 2 >= 0 and y + 2 < 8 and M[x-1][y+1] == n and M[x-2][y+2] == '.':
        M[x-1][y+1] = '.'
        return [True, x-2, y+2, M]
    elif x - 2 >= 0 and y - 2 >= 0 and M[x-1][y-1] == n and M[x-2][y-2] == '.':
        M[x-1][y-1] = '.'
        return [True, x-2, y-2, M]
    elif x + 2 < 8 and y - 2 >= 0 and M[x+1][y-1] == n and M[x+2][y-2] == '.':
        M[x+1][y-1] = '.'
        return [True, x+2, y-2, M]
    else:
        return [False]
import queue
f = open('input.txt')
z = int(f.readline().strip())
for i in range(z):
    Q = queue.Queue()
    M = []
    n1 = f.readline().strip()
    for q in range(8):
        s = f.readline().strip()
        M += [[i for i in s]]
        for j in range(8):
            if s[j] == n1:
                Q.put((q, j))
    res = 0
    while Q.qsize() > 0:
        k = 0
        x, y = Q.get()
        X, Y = x, y
        r = H(x, y, M, n1)
        while r[0]:
            k += 1
            r = H(r[1], r[2], r[3], n1)
        if k > res:
            res = k
            x_res, y_res = X, Y
    A = ['H', 'G', 'F', 'I', 'D', 'C', 'B', 'A']
    print(A[x_res], y_res+1, sep='')

#2021
kol, p = [i for i in input().split()]
kol = int(kol)
A = ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
p = [int(A.index(p[0])), int(p[1]) - 1]
M = []
for i in range(8):
    M += [['.'] * 8]
for i in range(kol):
    pos = input()
    M[A.index(pos[0])][int(pos[1]) - 1] = '*'
import queue
Q = queue.Queue()
Q.put((*p, M, []))
res = []
while Q.qsize() > 0:
    F = True
    x, y, M, kol = Q.get()
    if len(res) < len(kol):
        res = kol
    if '*' in M[x]:
        w = M[x].pos('*')
        M[x][w] = '.'
        Q.put((x, w, M, kol + [[x, w]]))
        F = False
    if F:
        for i in range(len(M)):
            if M[i][y] == '*':
                M[i][y] = '.'
                Q.put((i, y, M, kol + [[i, y]]))
                F = False
                break
    if F:
        while y > 0 and x > 0:
            x -= 1
            y -= 1
        if x < 8 and y < 8:
            for i in range(x, len(M)):
                if M[i][y] == '*':
                    M[i][y] = '.'
                    Q.put((i, y, M, kol + [[i, y]]))
                    F = False
                    break
                y += 1
                if y > 7:
                    break
    if F:
        while y < 7 and x < 7:
            x += 1
            y += 1
        if x < 8 and y < 8:
            for i in range(len(M) - 1, x + 1, -1):
                if M[i][y] == '*':
                    M[i][y] = '.'
                    Q.put((i, y, M, kol + [[i, y]]))
                    break
                y -= 1
                if y < 0:
                    break
print(len(res))
for i in res:
    print(A[i[0]], i[1] + 1, sep = '')