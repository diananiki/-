f = open('input.txt')
M = []
n, k, t = [int(i) for i in f.readline().split()]
for i in range(n):
    str, sim = [int(i) for i in f.readline().split('-')]
    M += [str * sim / k]
M.sort()
res, i = 0, 0
while res <= t:
    res, i = res + M[i], i + 1
print(i - 1)