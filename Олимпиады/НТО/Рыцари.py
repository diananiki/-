#5/20
r = int(input())
M = [int(i) for i in input().split()]
m1, lvl = [int(i) for i in input().split()]
while True:
    l = lvl
    if len(M) > 1 and M[m1 % r] == lvl and M[(m1-1) % r] == lvl:
        if m1 % r == 0:
            del M[0], M[-1]
            m1 = 0
        else:
            del M[m1 % r], M[(m1-1) % r]
            m1 -= 1
        lvl += 2
        r -= 2
    elif M[m1 % r] == lvl:
        del M[m1 % r]
        lvl += 1
        r -= 1
    elif M[(m1-1) % r] == lvl:
        del M[(m1-1) % r]
        lvl += 1
        m1 -= 1
        r -= 1
    if r == 0:
        print(1)
        exit()
    if lvl == l:
        print(len(M) + 1)
        exit()