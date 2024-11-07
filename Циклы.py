# Алгоритм поиска циклов(гамильтоновых)

f = open('input.txt')
n, m = [int(i) for i in f.readline().split()]
M = []
for i in range(n):
    M += [[0] * n]
for i in range(m):
    s1, s2, y = [int(i) for i in f.readline().split()]
    M[s1-1][s2-1], M[s2-1][s1-1] = 1, 1
res = [0]*(n+1)

def Cycle(s):
    global M
    global n
    global res
    if s[0] == s[-1] and len(s) != 1:
        if len(s) > 3:
            res[len(s)-1] += 1
            #print(s[:-1])
            return
        else:
            return None
    for j in range(n):
        if len(s) > 1 and j != s[-2] or len(s) == 1:
            if M[s[-1]][j] != 0:
                if not ((j in s) and s[0] != j):
                    Cycle(s + [j])

for i in range(n):
    Cycle([i])
r = 0
for i in range(1, len(res)):
    r += res[i]//(i*2)

print(r)



# Алгоритм поиска циклов(эйлеровых)

f = open('input.txt')
n, m = [int(i) for i in f.readline().split()]
M = []
for i in range(n):
    M += [[0] * n]
for i in range(m):
    s1, s2, y = [int(i) for i in f.readline().split()]
    M[s1-1][s2-1], M[s2-1][s1-1] = 1, 1
res2 = []
def Cycle(s):
    global M, n, res2
    if s[0] == s[-1] and len(s) != 1:
        if len(s) > 3:
            s2 = s[:-1]
            s2.sort()
            if s2 not in res2:
                res2 += [s2]
            return
        else:
            return None
    for j in range(n):
        if len(s) > 1 and j != s[-2] or len(s) == 1:
            if M[s[-1]][j] != 0:
                if not ((j in s) and s[0] != j):
                    Cycle(s + [j])

for i in range(n):
    Cycle([i])
#print(*res2)
P = []
for i in range(len(res2)):
    P += [res2[i]]
while len(P) > 1:
    x = P.pop()
    F = False
    for i in range(len(res2)):
        for j in res2[i]:
            if j in x:
                if F:
                    F = False
                    break
                F = True
                h = j
        if F:
            F = False
            t = x + res2[i]
            t.remove(h)
            t.sort()
            if t not in res2:
                res2 += [t]
                P += [t]

#print(*res2)
print(len(res2))