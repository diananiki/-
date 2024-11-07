#Алгоритм Прима

f = open('input.txt')
n, m = [int(i) for i in f.readline().split()]
M = []
for i in range(n):
    M += [[float('+inf')] * n]
for i in range(m):
    s1, s2, l = [int(i) for i in f.readline().split()]
    M[s1-1][s2-1], M[s2-1][s1-1] = l, l
for i in range(n):
    if max(M[i]) == 0:
        print(-1)
        exit()

def F(s):
    global M, n
    m = float('+inf')
    s1, s2 = 0, 0
    for i in s:
        for j in range(n):
            if M[i][j] < m:
                m = M[i][j]
                s2 = j
                s1 = i
                M[i][j], M[j][i] = float('+inf'), float('+inf')
    return s1, s2, m

G = [0] * n
R = 0
S = [0]
while min(G) == 0:
    s1, s2, r = F(S)
    G[s1], G[s2] = 1, 1
    R += r
    S += [s2]
print(R)