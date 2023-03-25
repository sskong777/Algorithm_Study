import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
t = min(nums)
answer = t

while True:
    c = 0
    answer += 1
    
    for num in nums:
        if answer % num == 0:
            c += 1
    
    if c >= 3:
        break
print(answer)