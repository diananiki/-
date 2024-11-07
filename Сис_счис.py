D1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
D2 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}


def To_b(a, b):
    global D2
    res = ''
    while a > 0:
        if a % b > 9:
            res = D2[a % b] + res
        else:
            res = str(a % b) + res
        a //= b
    return res


def To_10(a, b):
    global D1
    res = 0
    for i in range(1, len(a) + 1):
        if a[-1 * i] in ('ABCDEFGHIJK'):
            res += D1[a[-1 * i]] * b ** (i - 1)
        else:
            res += int(a[-1 * i]) * b ** (i - 1)
    return res