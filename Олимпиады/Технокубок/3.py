s = input()
str = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
M, i, b = [], 0, 0
while i < len(s):
    if s[i] in str and s[i + 1] in str and s[i + 2] in str and s[i] != s[i + 1] != s[i + 2]:
        M += [s[b:i + 2]]
        b = i + 2
        i += 1
    i += 1
M += [s[b:]]
print(*M)