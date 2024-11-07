s = input()
s = s.replace(' ', '')
s = list(s.lower())
res = ''
for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    if i in s:
        s.remove(i)
        res += i
        continue
print(*s, sep = '')
print(res)