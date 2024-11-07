Class = dict()
n = int(input())
g = []
for i in range(n-1):
    s1, s2 = [i for i in input().split()]
    Class[s2] = s1
    if s2 not in Class.values():
        g += [s2]
for j in range(len(g)):
    if g[j] not in Class.values():
        G = g[j]
        print(G)
        continue
for i in range(n-1):
    print(Class[G])
    G = Class[G]