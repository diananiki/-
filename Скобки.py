res = 0
def F(s):
    global res
    if s == '':
        return s
    i = 0
    if s[i] == '(':
        if ')' in s:
            l = s.index(')')
        else:
            s = s[0] + ')' + s[1:]
            res += 1
            l = 1
    elif s[i] == '[':
        if ']' in s:
            l = s.index(']')
        else:
            s = s[0] + ']' + s[1:]
            res += 1
            l = 1
    elif s[i] == '{':
        if '}' in s:
            l = s.index('}')
        else:
            s = s[0] + '}' + s[1:]
            res += 1
            l = 1
    elif s[i] == ')':
        s = '(' + s
        res += 1
        i = 0
        l = 1
    elif s[i] == ']':
        s = '[' + s
        res += 1
        i = 0
        l = 1
    elif s[i] == '}':
        s = '{' + s
        res += 1
        i = 0
        l = 1
    if l == 1:
        return s[i:l+1] + F(s[l+1:])
    for j in range(l // 2 + 1):
        if not(s[i+j] == '(' and s[l-j] == ')' or s[i+j] == '[' and s[l-j] == ']' or s[i+j] == '{' and s[l-j] == '}'):
            if l+1 < len(s):
                return s[0] + F(s[1:l]) + s[l] + F(s[l+1:])
            else:
                return s[0] + F(s[i:l]) + s[l]
s = input()
print(F(s))
print(res)