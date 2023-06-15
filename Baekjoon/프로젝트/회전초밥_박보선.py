import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

sushi_dict = {}
answer = [0 for _ in range(n + 1)]

for i in range(n):
    customer = list(map(int, input().split()))
    k = customer[0]
    l = customer[1:]
    
    for j in range(k):
        if l[j] not in sushi_dict:
            sushi_dict[l[j]] = deque([])
            sushi_dict[l[j]].append(i+1)
        else:
            sushi_dict[l[j]].append(i+1)
sushi = list(map(int, input().split()))
sushi = deque(sushi)

while sushi:
    a = sushi.popleft()
    
    if a not in sushi_dict:
        continue
    
    if len(sushi_dict[a]) != 0:
        b = sushi_dict[a].popleft()
        answer[b] += 1

print(*answer[1:])