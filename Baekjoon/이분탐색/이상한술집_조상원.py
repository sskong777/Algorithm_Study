import sys

n, total = map(int, input().split())
drinks = [int(sys.stdin.readline()) for i in range(n)]


l, r = 0, max(drinks)

while l < r:
    nums = 0
    mid = (l+r) // 2
    
    nums = sum([i // mid for i in drinks])
    
    if total <= nums:
        toRet = mid
        l = mid + 1
    else:
        r = mid - 1

print(toRet)