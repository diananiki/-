#f = open('input.txt')
from collections import deque
Mr = deque()
Ml = deque()
n = int(input())
#n = int(f.readline())
res = []
for i in range(n):
    s = input()
    #s = f.readline()
    if s[0] == '+':
        if len(Mr) == len(Ml):
            if len(Mr) == 0:
                Mr.appendleft(s.split()[-1])
            else:
                Mr.appendleft(Ml.pop())
                Ml.appendleft(s.split()[-1])
        else:
            Ml.appendleft(s.split()[-1])
    elif s[0] == '*':
        if len(Mr) == len(Ml):
            Mr.appendleft(s.split()[-1])
        else:
            Ml.append(s.split()[-1])
    else:
        res += [Mr.pop()]
        if len(Mr) < len(Ml):
            Mr.appendleft(Ml.pop())
print(*res, sep = '\n')