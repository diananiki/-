n = int(input())
train = [int(i) for i in input().split()]
M = []
res = []
index = 1
l = 0
for i in train:
    if i == index:
        r = 1
        while len(M) > 0 and M[-1] == index + 1:
            r += 1
            index += 1
            del M[-1]
        res += [[1, l + 1]]
        l = 0
        res += [[2, r]]
        index += 1
        if index in M:
            print(0)
            exit()
    else:
        M += [i]
        l += 1
for i in res:
    print(*i)