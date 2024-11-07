#поиск в ширину
import queue
Q = queue.Queue()
f = open('input3.txt')
n, m = [int(i) for i in f.readline().split()]
M = []
for i in range(n):
    M += [[0] * n]
for i in range(m):
    s1, s2, l = [int(i) for i in f.readline().split()]
    s1, s2 = min(s1, s2), max(s1, s2)
    M[s1-1][s2-1] = l
Q.put(0)
print(1)
while Q.qsize() != 0:
    x = Q.get()
    for j in range(n):
        if M[x][j] != 0:
            print(j+1)
            Q.put(j)

#поиск в глубину
S = []
f = open('input3.txt')
n, m = [int(i) for i in f.readline().split()]
M = []
for i in range(n):
    M += [[0] * n]
for i in range(m):
    s1, s2, l = [int(i) for i in f.readline().split()]
    s1, s2 = min(s1, s2), max(s1, s2)
    M[s1-1][s2-1] = l
S += [0]
print(1)
while len(S) != 0:
    x = S.pop()
    print(x+1)
    for j in range(n):
        if M[x][j] != 0:
            S.append(j)