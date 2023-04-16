import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
s = 1
e = trees[-1]
mid = 0
answer = 0
while s <= e:
    mid = (s + e) // 2
    t = 0
    
    for i in range(n):
        if trees[i] > mid:
            t += (trees[i] - mid)
        if t > m:
            break

    if t < m:
        e = mid - 1
    elif t >= m:
        answer = mid
        s = mid + 1
print(answer)