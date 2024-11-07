a = int(input())
b = int(input())
print((a + b) % 9)

#2021
d, r = [float(i) for i in input().split()]
r = int(r)
l = 0
res = '0,'
for i in range(r):
    d *= 4
    if int(d) == 0:
        l += 1
    else:
        l = 0
    res += str(int(d))
    if d >= 1:
        d -= int(d)
print(res[:len(res) - l])