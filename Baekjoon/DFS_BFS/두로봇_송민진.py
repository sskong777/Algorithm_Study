import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000000)

n, start, end = map(int, input().strip().split())
tree = [[] for _ in range(n+1)]
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]
tmp_total_d = 0
tmp_max_d = 0
for _ in range(n-1):
    node1, node2, d = map(int, input().strip().split())
    tree[node1].append(node2)
    tree[node2].append(node1)
    graph[node1][node2] = d
    graph[node2][node1] = d

def dfs(from_node, total_d, max_d):
    global tmp_total_d
    global tmp_max_d
    if from_node == end:
        tmp_total_d = total_d
        tmp_max_d = max_d

    else:
        for i in tree[from_node]:
            if graph[from_node][i] != int(1e9) and not visited[i]:
                visited[i] = True
                dfs(i, total_d+graph[from_node][i], max(graph[from_node][i], max_d))

visited[start] = True
dfs(start, 0, 0)
print(tmp_total_d - tmp_max_d)