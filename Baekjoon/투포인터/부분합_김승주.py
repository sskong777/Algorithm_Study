import sys
input = sys.stdin.readline

n, s = map(int,input().split())
numbers = list(map(int, input().rstrip().split()))

start, end = 0, 0
slide_sum = numbers[0]

ans = 1e9

while True:
    if slide_sum >= s:
        ans = min(ans, end-start+1)
        slide_sum -= numbers[start]
        start +=1
    else:
        end +=1
        if end == n:
            break
        slide_sum += numbers[end]

if ans == 1e9:
    print(0)
else:
    print(ans)