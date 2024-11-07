a, b, d = [int(i) for i in input().split()]
a, b = max(a, b), min(a, b)
if (a - b) % 2 == 0:
    print((a + b) // 2, min(((a + b) // 2) % d, d - ((a + b) // 2) % d))
else:
    c = min(((a + b - 1) // 2) % d, ((a + b + 1) // 2) % d, d - ((a + b - 1) // 2) % d, d - ((a + b + 1) // 2) % d)
    if ((a + b - 1) // 2) % d == c or d - ((a + b - 1) // 2) % d == c:
        print((a + b - 1) // 2, min(((a + b - 1) // 2) % d, d - ((a + b - 1) // 2) % d))
    else:
        print((a + b + 1) // 2, min(((a + b + 1) // 2) % d, d - ((a + b + 1) // 2) % d))