f = open('input.txt')
n = int(f.readline())
D = dict()
for i in range(n):
    s = f.readline().splitlines()[0]
    if s.lower() in D:
        D[s.lower()] = D[s.lower()] + '_' + s
    else:
        D[s.lower()] = s
s = f.readline()
res = 0
for i in s.split():
    F = False
    if i.lower() in D.keys():
        for j in D[i.lower()].split('_'):
            if i == j:
                F = True
        if not F:
            res += 1
    else:
        F = True
        for j in i:
            if j.isupper():
                if not F:
                    res += 1
                    break
                F = False
        if F:
            res += 1
print(res)