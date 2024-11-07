p = int(input())
n1 = min(100, p/100*8)
n2 = p/100*5
if int(n1) == n1:
    n1 = int(n1)
if int(n2) == n2:
    n2 = int(n2)
print(max(n1, n2))