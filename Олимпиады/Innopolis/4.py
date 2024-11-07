n = int(input())
res = 0
M = [int(i) for i in input().split()]
P = []
for i in range(len(M) - 2):
    P += [M[i] ^ M[i + 1]], [M[i + 1] ^ M[i + 2]]
for i in range(len(P) - 1):
    if P[i] < P[i+1]:
        res += 1
print(res)