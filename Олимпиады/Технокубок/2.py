f = open('input.txt')
n, m = [int(i) for i in f.readline().split()]
K, ma, j = [0] * 100, 0, 0
for i in range(m):
    k, l = [int(i) for i in f.readline().split()]
    l -= 1
    if K[l] == 0:
        K[l] = [k]
    else:
        K[l] += [k]
        K[l].sort()
    ma = max(ma, l + 1)
    j = max(j, len(K[l]))
K = K[:ma]
for i in range(1, (K[0][-1])):
    if i not in K[0]:
        K[0] += [i]
K[0].sort()
j = max(j, len(K[0]))
i = j - 1
Fl = False
Q = True
while Q:
    F = True
    i += 1
    q = -1
    for j in range(1, 101, i):
        q += 1
        if q >= len(K):
            break
        else:
            if q > 0:
                if j < K[q - 1][-1]:
                    F = False
                    break
            if j > K[q][0]:
                F = False
                break
    if F and not Fl:
        Fl = True
    elif F and Fl:
        print(-1)
        exit()
    elif not F and Fl:
        kv = i - 1
        Q = False
if kv == 0:
    print(-1)
else:
    if n % kv == 0:
        print(n // kv)
    else:
        print(n // kv + 1)