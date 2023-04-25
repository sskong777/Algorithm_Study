import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
lst = []


def backtrack(start, curr):
    global cnt
    if sum(curr) == m and len(lst) > 0:
        cnt += 1

    for i in range(start, n):
        lst.append(arr[i])
        backtrack(i+1, lst)
        lst.pop()


backtrack(0, lst)
print(cnt)
