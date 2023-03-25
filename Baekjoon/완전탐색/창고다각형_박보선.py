import sys
input = sys.stdin.readline

n = int(input())
p = 0
t = 0
e = 0
pillars = [0 for _ in range(1001)]
for i in range(n):
    l, h = map(int, input().split())
    pillars[l] = h
    if h > t:
        t = h
        p = l
    if e < l:
        e = l
cur = 0
answer = t
for i in range(p):
    if cur <= pillars[i]:
        cur = pillars[i]
    answer += cur
    
cur = 0
for i in range(e, p, -1):
    if cur <= pillars[i]:
        cur = pillars[i]
    answer += cur
    
print(answer)