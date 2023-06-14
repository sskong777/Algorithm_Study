import sys
input = sys.stdin.readline

n, m = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(m)]

count = 0
for i, j, k in space:
    if [i+1, j, k] in space and [i-1, j, k] in space and [i, j+1, k] in space and [i, j-1, k] in space and [i, j, k+1] in space and [i, j, k-1] in space:
        count += 1

print(count)
