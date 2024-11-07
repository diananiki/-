def Swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

res = []
def F(s, pos):
    global res
    if pos == len(s):
        res += [s]
    else:
        for i in range(pos, len(s)):
            F(Swap(s, i, pos), pos + 1)

F("QWER", 0)
print(*res, sep='\n')