import queue
Q1 = queue.Queue()
Q2 = queue.Queue()
s1 = input()
s2 = input()
for i in s1:
    if i == ' ':
        continue
    Q1.put((int(i)))
for i in s2:
    if i == ' ':
        continue
    Q2.put((int(i)))
#Q1.put((int(i) for i in input().split(' ')))
#Q2.put((int(i) for i in input().split(' ')))
h = 0
while Q1.qsize() > 0 and Q2.qsize() > 0:
    if h > 10**6:
        print('botva')
        exit()
    k1, k2 = Q1.get(), Q2.get()
    if k1 > k2 and not (k1 == 9 and k2 == 0) or k1 == 0 and k2 == 9:
        h += 1
        Q1.put((k1))
        Q1.put((k2))
    else:
        h += 1
        Q2.put((k1))
        Q2.put((k2))
if Q1.qsize() > 0:
    print('first', h)
else:
    print('second', h)