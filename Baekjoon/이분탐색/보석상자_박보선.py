import sys
input = sys.stdin.readline

n, m = map(int, input().split())

jewels = [int(input()) for _ in range(m)]
jewels.sort()

s = 1
e = jewels[-1]
mid = 0
answer = 0

while s <= e:
    cnt = 0
    mid = (s + e) // 2
    
    for i in range(m):
        cnt += jewels[i] // mid
        
        if jewels[i] % mid > 0:
            cnt += 1
        
        if cnt > n:
            break
    
    if cnt > n:
        s = mid + 1
    elif cnt <= n:
        answer = mid
        e = mid - 1
        
print(answer)