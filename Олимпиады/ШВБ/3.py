n, m = [int(i) for i in input().split()]
M = []
for i in range(n):
    M += [input()]
M = M[::-1] + M
for i in range(len(M)):
    M[i] = M[i][::-1] + M[i]
print(*M, sep = '\n')