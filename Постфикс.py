s = input()
M = []
for i in s:
    if i == ' ':
        continue
    if i in ['+', '-', '*']:
        a = int(M.pop())
        b = int(M.pop())
        if i == '+':
            M += [a + b]
        elif i == '-':
            M += [b - a]
        else:
            M += [a * b]
    else:
        M += [int(i)]
print(M[0])
