S = "2 2 2 + 2 2 2 + * - *"
op = ['*', '/', '-', '+']


def Calc(S):
    s = S.split(' ')
    M = []
    for i in s:
        if i == '+':
            B, A = float(M.pop()), float(M.pop())
            M.append(float(A + B))
        elif i == '-':
            B, A = float(M.pop()), float(M.pop())
            M.append(float(A - B))
        elif i == '*':
            B, A = float(M.pop()), float(M.pop())
            M.append(float(A * B))
        elif i == '/':
            B, A = float(M.pop()), float(M.pop())
            M.append(float(A / B))
        else:
            M.append(float(i))
    return M.pop()


def PostfixToInfix(S):
    # S = "2 2 2 + 2 2 2 * * - *"
    s = S.split(' ')
    M = []
    for i in s:
        if i == '+':
            B, A = M.pop(), M.pop()
            M.append(A + '+' + B)
        elif i == '-':
            B, A = M.pop(), M.pop()
            M.append(A + '-' + B)
        elif i == '*':
            B, A = M.pop(), M.pop()
            if B.find('+') != -1 or B.find('-') != -1 or B.find('/') != -1:
                if A.find('+') != -1 or A.find('-') != -1 or A.find('*') != -1 or A.find('/') != -1:
                    if (B.find('+') != 0 and B.find('*') < B.find('+')) and (
                            B.find('-') != 0 and B.find('*') < B.find('-')) and (
                            B.find('/') != 0 and B.find('*') < B.find('/')):
                        M.append('(' + A + ')' + '*' + B)
                    else:
                        M.append('(' + A + ')' + '*' + '(' + B + ')')
                else:
                    if (B.find('+') != 0 and B.find('*') < B.find('+')) and (
                            B.find('-') != 0 and B.find('*') < B.find('-')) and (
                            B.find('/') != 0 and B.find('*') < B.find('/')):
                        M.append(A + '*' + B)
                    else:
                        M.append(A + '*' + '(' + B + ')')
            elif A.find('+') != -1 or A.find('-') != -1 or A.find('*') != -1 or A.find('/') != -1:
                M.append('(' + A + ')' + '*' + B)
            else:
                M.append(A + '*' + B)
        elif i == '/':
            B, A = M.pop(), M.pop()
            if B.find('+') != -1 or B.find('-') != -1 or B.find('*') != -1:
                if A.find('+') != -1 or A.find('-') != -1 or A.find('*') != -1 or A.find('/') != -1:
                    if (B.find('+') != 0 and B.find('/') < B.find('+')) and (
                            B.find('-') != 0 and B.find('/') < B.find('-')) and (
                            B.find('*') != 0 and B.find('/') < B.find('*')):
                        M.append('(' + A + ')' + '/' + B)
                    else:
                        M.append('(' + A + ')' + '/' + '(' + B + ')')
                else:
                    if (B.find('+') != 0 and B.find('/') < B.find('+')) and (
                            B.find('-') != 0 and B.find('/') < B.find('-')) and (
                            B.find('*') != 0 and B.find('/') < B.find('*')):
                        M.append(A + '/' + B)
                    else:
                        M.append(A + '/' + '(' + B + ')')
            elif A.find('+') != -1 or A.find('-') != -1 or A.find('*') != -1 or A.find('/') != -1:
                M.append('(' + A + ')' + '/' + B)
            else:
                M.append(A + '/' + B)
        else:
            M.append(i)
    return M.pop()


def InfixToPostfix(W):
    def Parse(s):
        try:
            return float(s)
        except ValueError:
            return None

    def Separate(s):
        if Parse(s) is not None:
            return [s]
        beg = 0

        while True:
            io, ib = 0, s.find('(', beg) if s.find('(', beg) != -1 else float('+inf')
            i = [s.find(j, beg) if s.find(j, beg) != -1 else float('+inf') for j in op]
            io = min(i)
            if io < ib:
                left, right = s[:io], s[io + 1:]
                if left[0] == '(' and left[-1] == ')':
                    left = [left[1:-1]]
                else:
                    left = Separate(left)
                if right[0] == '(' and right[-1] == ')':
                    right = [right[1:-1]]
                else:
                    right = Separate(right)
                x = []
                x += left + [s[io]] + right
                return x
            p = 1
            while True:
                iob, icb = s.find('(', beg + 1) if s.find('(', beg + 1) != -1 else float('+inf'), \
                           s.find(')', beg + 1) if s.find(')', beg + 1) != -1 else float('+inf')
                beg = iob + 1
                p += 1
                if icb < iob:
                    p -= 2
                    beg = icb + 1
                    if p == 0:
                        break

    if Parse(W) is not None:
        return W
    w = Separate(W)
    for i in range(len(w)):
        if not (w[i] in op):
            w[i] = InfixToPostfix(w[i])
    i = 1
    while i < len(w):
        if w[i] in ["*", "/"]:
            w[i - 1] = w[i - 1] + w[i + 1] + w[i]
            del w[i:i + 2]
        else:
            i += 2
    i = 1
    while i < len(w):
        if w[i] in ["+", "-"]:
            w[i - 1] = w[i - 1] + w[i + 1] + w[i]
            del w[i:i + 2]
        else:
            i += 2
    return w[0]