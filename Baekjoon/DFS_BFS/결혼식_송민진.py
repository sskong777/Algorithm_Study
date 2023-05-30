import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
answer = 0
tree = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().strip().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node, depth):
    global answer
    for child in tree[node]:
        if depth > 1:
            break
        elif child != 1 and not visited[child]:
            visited[child] = True
            answer += 1
        dfs(child, depth+1)

dfs(1, 0)

print(answer)
