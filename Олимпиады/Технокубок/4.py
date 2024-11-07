f = open('input.txt')
n = int(f.readline())
M, m = [], []
for i in range(n):
    M += [str(f.readline())]
    m += [0]
for i in range(1, 10):
    if not (0 in m):
        break
    for j in range(10 - i):
        if not (0 in m):
            break
        for d in range(len(M)):
            if m[d] == 0:
                Fl = True
                s = M[d][j:j + i]
                for q in range(len(M)):
                    if s in M[q] and q != d:
                        Fl = False
                        break
                if Fl:
                    m[d] = s
print(*m, sep="\n")