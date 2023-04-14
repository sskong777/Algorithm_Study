# [2792] 보석상자
n, k = map(int, input().split())
colors = [int(input()) for _ in range(k)]

start, end = 1, max(colors)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for color in colors:
        if color % mid == 0:
            total += color // mid
        else:
            total += (color // mid) + 1
    if total > n:
        start = mid + 1
    else:
        end = mid - 1
print(start)
