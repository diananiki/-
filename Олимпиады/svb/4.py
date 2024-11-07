n, m, k = [int(i) for i in input().split()]
m1, b = [], []
for i in range(n):
    m1 += [[int(i) for i in input().split()]]
    b += [[0] * m]
for i in range(n):
    j = 0
    if j <= m - 2 and m1[i][j] <= m1[i][j+1]:
        b[i][j], b[i][j + 1] = [1], [1]
        j += 1
        while j <= m - 2 and m1[i][j] <= m1[i][j+1]:
            b[i][j], b[i][j + 1] = [1], [1]
            j += 1
        j += 1
print(b)

