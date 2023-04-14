import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
s, e = 1, max(li)
ans = 0
while s <= e:
    m = (s+e)//2
    t = sum(n//m for n in li)
    if t >= k:
        ans = m
        s = m+1
    else:
        e = m-1
print(ans)