from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, f().split())
    graph[s].append(e)
    

d = [-1] * (n+1)
d[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    
    for next in graph[now]:
        if d[next] == -1:
            d[next] = d[now] + 1
            q.append(next)
            
check = False

for i in range(1, n + 1):
    if d[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)