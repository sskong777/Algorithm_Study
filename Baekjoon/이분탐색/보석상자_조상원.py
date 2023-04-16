import sys

k, c = map(int, input().split())

jewels = [int(sys.stdin.readline()) for _ in range(c)]

l, r = 1, max(jewels)
toRet = 1

while l  <= r:
    mid = (l + r) // 2
    curr = 0
    for j in jewels:
        curr += j// mid
        if j % mid != 0:
            curr += 1

    if k < curr:
        l = mid + 1
    else:
        r = mid - 1


print(l)