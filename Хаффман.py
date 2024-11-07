from queue import PriorityQueue
s = input()
D = dict()
res = dict()
Q = PriorityQueue()
for i in s:
    D[i] = D.get(i, 0) + 1
for i in D.items():
    Q.put((i[1], [i[0]]))
while Q.qsize() > 1:
    h1, b1 = Q.get()
    h2, b2 = Q.get()
    Q.put((h1+h2, b1+b2))
    for i in b1:
        res[i] = '0' + res.get(i, '')
    for i in b2:
        res[i] = '1' + res.get(i, '')
for i in res.items():
    print(i[1], '-', i[0])