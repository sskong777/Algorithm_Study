import sys

input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ret = []

for _ in range(m):
  i, j = map(int, input().split())  
  graph[i].append(j)
  graph[j].append(i)

cnt=0
def dfs(v):
  global cnt
  cnt+=1
  visited[v] = True

  if v == b:
    ret.append(cnt)

  for i in graph[v]:
    if not visited[i]:
      dfs(i)

dfs(a)

if len(ret)==0:
  print(-1)
else:
  print(ret[0]-1)