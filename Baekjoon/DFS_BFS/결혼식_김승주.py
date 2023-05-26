from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]

for i in range(m):
    a,b  = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

visited= [False] * (n+1)

def bfs():
    q = deque([])

    count =0
    visited[1] = True
    depth =1
    for i in friends[1]:
        visited[i] = True
        count+=1
        q.append((i,depth))

    while q:
        nx, dep = q.popleft()

        if dep >= 2 :
            break

        for i in friends[nx]:
            if not visited[i]:
                count+=1
                visited[i] = True
                q.append((i, dep+1))

    print(count)
bfs()
