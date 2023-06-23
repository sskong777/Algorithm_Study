import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [input().rstrip() for _ in range(n)]

c = [input().rstrip() for _ in range(m)]

d = dict()

for i, v in enumerate(arr):
    d[str(int(i)+1)] = v
    d[v] = str(int(i)+1)


# print(arr)
# print(c)
# print(d)


for l in c:
    print(d[l])