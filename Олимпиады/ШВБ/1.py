n = int(input())
M = []
for i in range(n):
    M += [int(input())]
d = int(input())
D = dict()
m = float('+inf')
for j in M:
    D[j] = min(j - j // d * d, (j // d + 1) * d - j)
    if D[j] == 0:
        print(len(D), 0)
        break
    if D[j] < m:
        m = D[j]
        res = [len(D), D[j]]
print(*res)

#2021
s = input()
res = 0
for i in range(len(s)-1):
    if (int(s[i]) + int(s[i+1])) % 3 == 0:
        res += 1
print(res)