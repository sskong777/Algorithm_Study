import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    qu = input().rstrip()
    if qu.isdigit():
        print(dict[int(qu)])
    else:
        print(dict[qu])
