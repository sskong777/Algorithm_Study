import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))


temp = nums[0]
answer = 0
s = 0
e = 0


# while e != n - 1:
#     if temp == m:
#         answer += 1
#         e += 1
#         temp += nums[e]
#     elif temp > m:
#         temp -= nums[s]
#         s += 1
#     elif temp < m:
#         e += 1
#         temp += nums[e]


while True:
    if temp == m:
        answer += 1
        
        
    if temp > m:
        temp -= nums[s]
        s += 1
    elif e == n - 1:
        break
    elif temp <= m:
        e += 1
        temp += nums[e]

print(answer)