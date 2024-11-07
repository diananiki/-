f = open('input.txt')
n = int(f.readline())
u, M, I, res, pr = 0, [], [], [], []
for i in range(n):
    a, b = [i for i in f.readline().split()]
    b = int(b)
    if b == 1:
        u += 1
    M += [a]
    I += [b]
    pr += [str(i + 1)]
F = False
i, z = 0, n
while i < n:
    if i < u:
        for q in range(n):
            if I[q] == 1:
                if M[q] in pr and int(M[q]) > u or not (M[q] in pr):
                    for j in range(1, u + 1):
                        if str(j) in M:
                            F = True
                        else:
                            res += [['move', M[q], j]]
                            I[q] = 11
                            M[q] = str(j)
                            i += 1
                            F = False
                            break
                    if F:
                        for a in range(1, n + 1):
                            if str(a) in M and I[M.index(str(a))] == 0:
                                ind = M.index(str(a))
                                break
                        if str(z) not in M:
                            res += ['move', M[ind], n], ['move', M[q], a]
                            M[q], M[ind] = str(a), str(n)
                            i += 1
                            I[q], I[ind] = 11, 10
                            z -= 1
                            break
                        else:
                            res += ['move', M[q], n + 1], ['move', M[ind], M[q]], ['move', n + 1, a]
                            M[q], M[ind] = M[ind], M[q]
                            i += 1
                            I[q], I[ind] = 11, 10
                            break
                else:
                    i += 1
                    I[q] = 11
                    break
    else:
        for q in range(n):
            if I[q] == 0:
                if M[q] in pr and int(M[q]) <= n:
                    i += 1
                    I[q] = 10
                    break
                else:
                    for j in range(u + 1, n + 1):
                        if not (str(j) in M):
                            res += [['move', M[q], j]]
                            I[q] = 10
                            M[q] = str(j)
                            i += 1
                            break
            elif I[q] == 10:
                i += 1
print(len(res))
for i in range(len(res)):
    print(*res[i])