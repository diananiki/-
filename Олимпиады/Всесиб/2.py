f = open('input.txt')
n, M, res = int(f.readline()), [], 0
for i in range(n):
    x, y = [int(i) for i in f.readline().split()]
    M += [[x, y]]
for i in range(n):
    for j in range(i + 1, n):
        for q in range(j + 1, n):
            A = [((M[i][0] - M[j][0]) ** 2 + (M[i][1] - M[j][1]) ** 2),
                 ((M[i][0] - M[q][0]) ** 2 + (M[i][1] - M[q][1]) ** 2),
                 ((M[q][0] - M[j][0]) ** 2 + (M[q][1] - M[j][1]) ** 2)]
            A.sort()
            if A[2] == A[0] + A[1]:
                res += 1
print(res)