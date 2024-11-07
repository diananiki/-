import math
n = int(input())
M = [0] * n
for i in range(n):
    M[i] = [0] * (n - 1)
for i in range(n - 1):
    inp = [int(i) for i in input().split()]
    for j in range(n):
        M[j][i] = inp[j]
D = [0] * n
for i in range(1, n + 1):
    for j in range(n):
        if i not in M[j]:
            if D[j] > 0:
                D[j] = False
            else:
                D[j] = i
V = [i for i in range(1, n + 1)]
mn = 1
for i in D:
    if i and i in V:
        V.remove(i)
        mn *= D.count(i)
print(n - len(V), math.factorial(len(V)) * mn)