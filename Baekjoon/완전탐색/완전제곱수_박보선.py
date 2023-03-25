import sys
input = sys.stdin.readline

cnt = 0
n = int(input())

for i in range(1, 501):
    for j in range(i + 1, 501):
        r = j**2 - i**2
        if r == n:
            cnt += 1
            break
        elif r > n:
            break
        
print(cnt)
        