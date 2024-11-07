#номер лунки и расстояние
x, y = [int(i) for i in input().split()]
a, b = [0, -1 / (3 ** (1 / 2)), -1, -3 ** (1 / 2), -1, 3 ** (1 / 2), 1, 1 / (3 ** (1 / 2))], [1, 1, 1, 1, 0, 1, 1, 1]
c = [a[i] * x - b[i] * y for i in range(8)]
M0, M1, M = [[0, 0, 1], [50, 0, 2], [100, 0, 3], [0, 50, 4], [50, 50, 5], [100, 50, 6]], [], []
for i in range(-3, 4):
    for A in M0:
        if A[2] < 4:
            A[2] += 3
        else:
            A[2] -= 3
        M1 += [[A[0], A[1] + 51 * i, A[2]]]
for i in range(-3, 4):
    for A in M1:
        if A[2] == 3 or A[2] == 6:
            A[2] -= 2
        elif A[2] == 1 or A[2] == 4:
            A[2] += 2
        M += [[A[0] + 101 * i, A[1], A[2]]]
o, l = 10000, 0
for [m, n, k] in M:
    for i in range(8):
        if (a[i] == 0 and n <= -c[i] / b[i] <= n + 1 or
                b[i] == 0 and m <= -c[i] / a[i] <= m + 1 or
                a[i] * b[i] != 0 and
                (abs((-c[i] - a[i] * m) / b[i] - n - 0.5) <= 0.5 or
                 abs((-c[i] - a[i] * (m + 1)) / b[i] - n - 0.5) <= 0.5 or
                 abs((-c[i] - b[i] * n) / a[i] - m - 0.5) >= 0.5 or
                 abs((-c[i] - b[i] * (n + 1)) / a[i] - m - 0.5) >= 0.5)):
            if (abs(m - x)**2 + abs(n - y)**2)**0.5 < o:
                o = (abs(m - x)**2 + abs(n - y)**2)**0.5
                l = k
if o < 10000:
    print('yes', l, o)
else:
    print('no')