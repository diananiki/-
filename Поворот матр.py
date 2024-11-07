# Program to transpose a matrix using a nested loop
import copy
def rotcontrclc(m):
    r = []
    i = 0
    for _ in m:
        listToAdd = [item[i] for item in m]
        r.append(listToAdd)
        i += 1
    return r[::-1]
def rotlayer(m, ind):
    r = copy.deepcopy(m)
    m2 = rotcontrclc(m)
    for i in range(len(m)):
        for j in range(len(m)):
            if ind <= i <= len(m) - ind - 1 and ind <= j <= len(m) - ind - 1 and (
                    i == ind or len(m) - i - 1 == ind or j == ind or len(m) - j - 1 == ind):
                r[i][j] = m2[i][j]
    return r
def sumcolumn(m, ind):
    res = 0
    for i in range(len(m)):
        res += m[i][ind]
    return res
X = [[9, 10, 8, 4],
     [5, 10, 11, 2],
     [7, 2, 1, 4],
     [3, 10, 2, 1]]

res = float('-inf')
k = 0
n = 0
resm = []

def F(m, lvl, p):
    global res, k, n, resm
    if lvl <= len(m) // 2:
        m1 = copy.deepcopy(m)
        for i in range(4):
            F(m1, lvl + 1, (4 - i) % 4 + p)
            m1 = rotlayer(m1, lvl)
    else:
        for j in range(len(m)):
            w = sumcolumn(m, j)
            if w > res or (w == res and p < k):
                res = w
                n = j
                k = p
                resm = copy.deepcopy(m)

F(X, 0, 0)
print(k, n + 1, res)
for i in resm:
    print(*i)