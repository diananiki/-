#set - множество; add - добавить; discard - удалить.   list - список
n1 = int(input())
a = set(int(i) for i in input().split())
n2 = int(input())
b = set(int(i) for i in input().split())
d = a ^ b
c = list(d)
c.sort()
print(len(c))
print(*c)