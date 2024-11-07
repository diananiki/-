m, n, h = 10, 10, 10
import queue
Q = queue.Queue()
D = dict()
D['x'] = []
D['y'] = []
D['z'] = []
Q.put([int(i) for i in input().split()] + [0, D])
xf, yf, hf = [int(i) for i in input().split()]
p = int(input())
P = []
for i in range(p):
    P += [[int(i) for i in input().split()]]
while Q.qsize() > 0:
    x, y, z, k, D = Q.get()
    D['x'] = D.get('x', []) + [x]
    D['y'] = D.get('y', []) + [y]
    D['z'] = D.get('z', []) + [z]
    if x == xf and y == yf and z == hf:
        print(k)
        exit()
    if x + 1 < n and [x + 1, y, z] not in P and [x + 1] not in D['x']:
        Q.put((x+1, y, z, k+1, D))
    if x - 1 > -1 and [x - 1, y, z] not in P and x - 1 not in D['x']:
        Q.put((x-1, y, z, k+1, D))
    if y + 1 < m and [x, y + 1, z] not in P and y + 1 not in D['y']:
        Q.put((x, y+1, z, k+1, D))
    if y - 1 > -1 and [x, y - 1, z] not in P and y - 1 not in D['y']:
        Q.put((x, y-1, z, k+1, D))
    if z + 1 < h and [x, y, z + 1] not in P and z + 1 not in D['z']:
        Q.put((x, y, z+1, k+1, D))
    if z - 1 > -1 and [x, y, z - 1] not in P and x - 1 not in D['z']:
        Q.put((x, y, z-1, k+1, D))
print('NO')