import sys
input = sys.stdin.readline

a,b,n,w = map(int,input().split())

# 가능한 해가 2개 이상이거나 없을 경우 -1
ans = []
for i in range(1,n):
    if i*a +(n-i)*b == w:
        ans.append(i)
if len(ans) == 0 or len(ans) >1:
    print(-1)
    exit()
print(ans[0], n-ans[0])
