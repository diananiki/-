bank = dict()

f = open('input.txt')

#n = int(input())
n = int(f.readline())

res = []
for i in range(n):

    #s = input().split()
    s = f.readline().split()

    if s[0] == 'DEPOSIT':
        bank[s[1]] = bank.get(s[1], 0) + int(s[2])
    elif s[0] == 'WITHDRAW':
        bank[s[1]] = bank.get(s[1], 0) - int(s[2])
    elif s[0] == 'TRANSFER':
        bank[s[1]] = bank.get(s[1], 0) - int(s[3])
        bank[s[2]] = bank.get(s[2], 0) + int(s[3])
    elif s[0] == 'INCOME':
        for k, summ in bank.items():
            if summ > 0:
                bank[k] += int(summ*(int(s[1])/100))
    else:
        res += [bank.get(s[1], 'ERROR')]
print(*res, sep = '\n')