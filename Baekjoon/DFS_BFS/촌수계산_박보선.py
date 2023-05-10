import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(e, c):
    global answer
    c += 1
    visited[e] = True
    
    if e == b:
        answer = c
    
    for i in graph[e]:
        if not visited[i]:
            dfs(i, c)
            
n = int(input())
a, b = map(int, input().split())
m = int(input())
answer = 0
graph = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(m):
    q, w = map(int, input().split())
    graph[q].append(w)
    graph[w].append(q)
    
if len(graph[a]) == 0:
    print(-1)
    exit()
    
dfs(a, 0)

if answer == 0:
    print(-1)
else:
    print(answer - 1)