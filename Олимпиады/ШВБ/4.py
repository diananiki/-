f = open('input.txt')
x, y, z = [float(i) for i in f.readline().split()]
n = int(f.readline())
max_tg = float('-inf')
res = 1
for i in range(n):
    x1, y1, z1 = [float(i) for i in f.readline().split()]
    if (z1 - z)/(((x - x1) ** 2 + (y - y1) ** 2) ** 0.5) > max_tg:
        max_tg = (z1 - z)/(((x - x1) ** 2 + (y - y1) ** 2) ** 0.5)
        res = i+1
print(res)