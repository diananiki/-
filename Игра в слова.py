f = open('input.txt')
t, w = [int(i) for i in f.readline().split()]
res = [0] * t
D = dict()
for i in range(w):
    K, W = [i for i in f.readline().split()]
    if D.get(W, 0) == 0:
        D[W] = K
        res[int(K) - 1] += 1
    else:
        res[int(D.get(W)) - 1] -= 1
        D[W] = K
        res[int(K) - 1] += 1
print(*res)