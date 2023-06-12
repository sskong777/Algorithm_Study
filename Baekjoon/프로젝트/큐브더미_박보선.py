import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cube = [list(map(int, input().split())) for _ in range(m)]
answer = 0
for i, j, k in cube:
    if [i+1, j, k] in cube and [i-1, j, k] in cube and [i, j+1, k] in cube and [i, j-1, k] in cube and [i, j, k+1] in cube and [i, j, k-1] in cube:
        answer += 1

print(answer)