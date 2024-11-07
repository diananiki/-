M = [int(i) for i in input().split()]
M.sort()
for i in range(len(M)):
    diag = M[i]
    m = M[:i] + M[i+1:]
    m1, m2 = m[:2] + [diag], m[2:] + [diag]
    if sum(m1) > 2 * max(m1) and sum(m2) > 2 * max(m2):
        print(diag)
        print(*m1[:2])
        print(*m2[:2])
        exit()
    m1, m2 = [m[0]] + [m[-1]] + [diag], [m[1]] + [m[-2]] + [diag]
    if sum(m1) > 2 * max(m1) and sum(m2) > 2 * max(m2):
        print(diag)
        print(*m1[:2])
        print(*m2[:2])
        exit()
    m1, m2 = [m[0]] + [m[-2]] + [diag], [m[1]] + [m[-1]] + [diag]
    if sum(m1) > 2 * max(m1) and sum(m2) > 2 * max(m2):
        print(diag)
        print(*m1[:2])
        print(*m2[:2])
        exit()
print(0)