import sys

n, m = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
l, r = 0, max(trees)

while l < r:
    mid = (l + r) // 2
    curr = sum([i - mid for i in  trees if i > mid])

    if curr < m:
        r = mid
    else:
        toRet=mid
        l = mid+1
print(toRet)
        
    