import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = {}
countList = [0] * n

for i in range(n):
    elements = map(int, input().split()[1:])
    for j in elements:
        li[j] = li.get(j, [])
        li[j].append(i)

orderList = map(int, input().split())

for i in orderList:
    if i in li:
        indices = li[i]
        index_to_remove = indices.pop(0)
        countList[index_to_remove] += 1
        if len(indices) == 0:
            del li[i]

print(*countList)
