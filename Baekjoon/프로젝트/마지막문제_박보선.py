import sys
input = sys.stdin.readline

n = int(input())

level = list(map(int, input().split()))
level.sort()

temp = 0
x = 0

for i in range(n-1):
    target = (level[i] + level[i + 1]) // 2
    
    if target != level[i]:
        minVal = min(target - level[i], level[i + 1] - target)
        if minVal > x:
            temp = target
            x = minVal
            
if temp == 0:
    print(-1)
else:
    print(temp)