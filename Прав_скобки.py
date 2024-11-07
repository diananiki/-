s = input()
M = []
for i in s:
    if i in ['(', '[', '{']:
        M += [i]
    else:
        if len(M) == 0:
            print('no')
            exit()
        else:
            if i == ')' and M[-1] == '(' or i == ']' and M[-1] == '[' or i == '}' and M[-1] == '{':
                del M[-1]
            else:
                print('no')
                exit()
if len(M) == 0:
    print('yes')
else:
    print('no')