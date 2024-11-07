f = open('input.txt')
n, m = [int(i) for i in f.readline().split()]
M, F, P, Fl = [], [], [], []
for i in range(n):
    M += [[int(0)] * n]
    F += [float('+inf')]
    P += [[]]
    Fl += [True]
for i in range(m):
    s1, s2, l = [int(i) for i in f.readline().split()]
    M[min(s1, s2) - 1][max(s1, s2) - 1] = l
F[0] = 0
s, si = float('+inf'), 0
while True:
    for i in range(n):
        if Fl[i] and s > F[i]:
            s = F[i]
            si = i
    if si == n-1:
        print(F[si])
        print(*P[si])
        exit()
    if s == float('+inf'):
        print('-1')
        exit()
    for i in range(n):
        if M[si][i] > 0:
            F[i] = min(F[i], M[si][i]+F[si])
            P[i] = P[si] + [si+1]
    Fl[si], s, si = False, float('+inf'), 0