import sys

input = sys.stdin.readline

n, m = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(m)]
t = 0


for i, j, k in arr:
    if [i+1, j, k] in arr and [i-1, j, k] in arr and [i, j+1, k] in arr and [i, j-1, k] in arr and [i, j, k+1] in arr and [i, j, k-1] in arr:
        t += 1

print(t)
