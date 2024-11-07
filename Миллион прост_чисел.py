n, M = 1299720, []
prime = [True] * (n + 1)
prime[0] = prime[1] = False
for i in range(2, n + 1):
    if not prime[i]:
        continue
    else:
        M += [i]
    for j in range(i * i, n + 1, i):
        prime[j] = False
n = int(input())
print(M[n-1])