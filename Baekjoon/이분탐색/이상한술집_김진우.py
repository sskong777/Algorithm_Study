import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

left = 0
right = arr[-1]
ans = 0
while left <= right :
    mid = (left + right) //2
    cnt = 0
    for i in arr:
        tmp = i // mid
        cnt += tmp

    if cnt >= k:
        left = mid +1
        ans = mid
    else:
        right = mid -1


print(ans)
