import sys
input = sys.stdin.readline

n = int(input())
cover = [0] * 1000
guards = []
for _ in range(n):
    start, end = map(int, input().strip().split())
    guards.append([start, end])
    for k in range(end - start):
        cover[start + k] += 1

max_cover = 0
for i in range(n):
    tmp = cover.copy()
    for j in range(guards[i][1] - guards[i][0]):
        tmp[guards[i][0]+j] -= 1

    cnt = 0
    for point in range(1000):
        if tmp[point] > 0:
            cnt += 1
    max_cover = max(max_cover, cnt)

print(max_cover)