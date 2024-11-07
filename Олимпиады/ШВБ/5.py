f = open('input.txt')
n = int(f.readline())
D = dict()
for i in range(n):
    j, v = [i for i in f.readline().split()]
    if len(D) > 0:
        pr = ''
        for a in v:
            pr += a
            for p in D.values():
                if p[1] == pr:
                    print('NO', p[0] + 1)
                    s = input()
                    exit()
                elif v == p[1][:min(len(p[1]), len(v))]:
                    print('NO', i + 1)
                    s = input()
                    exit()
    D[j] = [i, v]
s = f.readline()
print('YES')
b = 0
while '1' in s or '0' in s:
        for k in D.items():
            if s[b:len(k[1][1]) + b] == k[1][1]:
                s = s[:b] + k[0] + s[len(k[1][1]) + b:]
                b += 1
                break
print(s)

#2021
n = int(input())
res = []
for i in range(n):
    v, p, z = [int(i) for i in input().split()]
    res += [[v, p * z / 100, i]]
    for j in range(len(res) - 1):
        res += [[res[j][0] + v, res[j][1] + p * z // 100] + res[j][2:] + [i]]
m = int(input())
mi = float('+inf')
o = []
for i in range(len(res)):
    if res[i][1] >=m:
        if res[i][0] <= mi and (len(res[i][2:]) < len(o)or len(o) == 0):
            mi = res[i][1]
            o = res[i][2:]
for i in o:
    print(i + 1, end=' ')