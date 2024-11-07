import copy
n = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
S1, S2 = [[A, B, []]], []
F = False
for i in range(n):
    a, b = [int(i) for i in input().split()]
    if len(S1) != 0:
        for c in range(len(S1)):
            if a in S1[c][0] and b in S1[c][1]:
                w = copy.copy(S1[c][0])
                w.remove(a)
                S2 += [[]]
                S2[c].append(w)
                w = copy.copy(S1[c][1])
                w.remove(b)
                S2[c].append(w)
                S2[c].append([*S1[c][2] + [a, b]])
                F = True
                res = S2[c][2]
            if b in S1[c][0] and a in S1[c][1]:
                w = copy.copy(S1[c][0])
                w.remove(b)
                S2 += [[]]
                S2[-1].append(w)
                w = copy.copy(S1[c][1])
                w.remove(a)
                S2[-1].append(w)
                S2[-1].append([*S1[c][2] + [b, a]])
                F = True
                res = S2[-1][2]
            if len(S2) == 0:
                F = False
        S1 = []
    else:
        for c in range(len(S2)):
            if a in S2[c][0] and b in S2[c][1]:
                w = copy.copy(S2[c][0])
                w.remove(a)
                S1 += [[]]
                S1[c].append(w)
                w = copy.copy(S2[c][1])
                w.remove(b)
                S1[c].append(w)
                S1[c].append([*S2[c][2] + [a, b]])
                F = True
                res = S1[c][2]
            if b in S2[c][0] and a in S2[c][1]:
                w = copy.copy(S2[c][0])
                w.remove(b)
                S1 += [[]]
                S1[-1].append(w)
                w = copy.copy(S2[c][1])
                w.remove(a)
                S1[-1].append(w)
                S1[-1].append([*S2[c][2] + [b, a]])
                F = True
                res = S1[-1][2]
            if len(S1) == 0:
                F = False
        S2 = []
if F:
    print('YES')
    for i in range(0, len(res) - 1, 2):
        print(*res[i:i+2])
else:
    print('NO')