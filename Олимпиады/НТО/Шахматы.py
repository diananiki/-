x = int(input())
y = int(input())
res = 0
x, y = max(x, y), min(x, y)
for i in [x, y]:
    if i in [3, 4, 5, 6]:
        res += 4
    elif i in [1, 8, 2, 7]:
        res += 2
        if i in [1, 8]:
            if 7 > x > 2 or 7 > y > 2:
                res -= 2
            else:
                res -= 1
print(res)