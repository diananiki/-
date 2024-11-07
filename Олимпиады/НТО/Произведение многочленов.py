n = int(input())
M = [0] * (n+2)
p = [int(i) for i in input().split()]
for i in range(len(p)):
    M[i+1] += p[i]
    M[i] += p[i]
print(*M)