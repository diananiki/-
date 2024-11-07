def S(n):
    return n + 1, n * 2, n * 3


from functools import lru_cache


@lru_cache(None)
def F(n):
    if 43 <= n <= 72:
        return False, [0]
    if n > 72:
        return True, [1]

    children = [F(x) for x in S(n)]
    win, steps, minsteps = not all(child[0] for child in children), [], [0] * 100
    for child in children:
        if child[0] != win:
            steps += [i + win for i in child[1]]
            if len(child[1]) < len(minsteps):
                minsteps = [i + win for i in child[1]]
    if win:
        steps = minsteps

    return win, list(set(steps))


for i in range(42, 0, -1):
    print(i, F(i))