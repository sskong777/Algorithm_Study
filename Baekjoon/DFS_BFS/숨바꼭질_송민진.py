from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
tmp = []

def bfs(start, end):
    queue = deque()
    queue.append((start, 0))  # 시작 위치와 거리(시간)를 큐에 추가
    visited[start] = True

    while queue:
        node, depth = queue.popleft()
        if node == end:
            tmp.append(depth)
            return

        next_positions = [node-1, node+1, node*2]
        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, depth+1))

bfs(n, k)
print(min(tmp))
