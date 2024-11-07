f = open('input.txt')
n = int(f.readline())
R = dict()
res = []
head = []
for i in range(n-1):
    s, p = [i for i in f.readline().split()]
    if R.get(p, 0) == 0:
        R[p] = [s]
    else:
        R[p] += [s]
    if s in head:
        head.remove(s)
    if sum([p in x for x in R.values()]) == 0 and p not in head:
        head += [p]
head = head[0]

def F(child, i):
    global res, R
    res += [child + ' ' + str(i)]
    if child in R.keys():
        for ch in R[child]:
            F(ch, i+1)

F(head, 0)
print(*sorted(res), sep = '\n')