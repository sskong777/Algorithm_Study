import sys


def dfs(x):
    for i in li[x]:
        if visited[i] == 0:
            visited[i] = visited[x]+1
            dfs(i)


input = sys.stdin.readline

n = int(input())
target_x, target_y = map(int, input().split())
m = int(input())

li = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    li[x].append(y)
    li[y].append(x)

visited = [0] * (n+1)

dfs(target_x)
print(visited[target_y] if visited[target_y] > 0 else -1)
