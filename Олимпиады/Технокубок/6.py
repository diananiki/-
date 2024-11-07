f = open('input.txt')
s, r = [int(i) for i in f.readline().split()]
M = [[0] * s for temp in range(s)]
for i in range(r):
    s1, s2 = [int(i)-1 for i in f.readline().split()]
    M[s1][s2], M[s2][s1] = 1, 1
res, n = [], 0
while True:
    for i in range(len(M)):
        if sum(M[i]) % 2 == 0 and sum(M[i]) > 0:
            while 1 in M[i]:
                j = M[i].index(1)
                s1 = j + 1
                M[i][j], M[j][i] = 0, 0
                j = M[i].index(1)
                s2 = j + 1
                M[i][j], M[j][i] = 0, 0
                res += [[s1, i + 1, s2]]
        elif sum(M[i]) > 1:
            n += 1
    if n > 0:
        for i in range(len(M)):
            if sum(M[i]) > 1:
                s1 = M[i].index(1) + 1
                M[i][M[i].index(1)], M[M[i].index(1)][i] = 0, 0
                s2 = M[i].index(1) + 1
                M[i][M[i].index(1)], M[M[i].index(1)][i] = 0, 0
                res += [[s1, i + 1, s2]]
        n = 0
    else:
        break
print(len(res))
for x in res:
    print(*x)

#функция поиска связей в циклах
f = open('input.txt')
s, r = [int(i) for i in f.readline().split()]
M = [[0] * s for temp in range(s)]
for i in range(r):
    s1, s2 = [int(i)-1 for i in f.readline().split()]
    M[s1][s2], M[s2][s1] = 1, 1
def F(n):
    global M
    roads = 0
    res = list(n)
    while len(n) > 0:
        for j in n:
            for i in range(s):
                if M[j][i] == 1:
                    roads += 1
                    if i not in res:
                        n += [i]
                        res += [i]
            n.remove(j)
    return [res, roads // 2]
r = 0
Fl = [True] * s
for i in range(s):
    if Fl[i]:
        RES = F([i])
        RES, R = RES[0], RES[1]
        for j in RES:
            Fl[j] = False
        r += R // 2
print(r)