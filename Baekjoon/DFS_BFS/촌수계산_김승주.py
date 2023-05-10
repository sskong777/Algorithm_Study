
import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 전체 사람의 수

x, y = map(int, input().split())
peoples = [ [] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    p_x, c_y = map(int, input().split()) # 양방향 그래프 
    peoples[c_y].append(p_x) # 부모 연결 표시
    peoples[p_x].append(c_y) # 자식 연결 표시 

visited = [False] * (n+1)
def bfs(x):
    
    q = deque([(x,0)])

    while q:
        n_x , count = q.popleft()
        
        if n_x == y:
            return count 
    
        for i in peoples[n_x]:
            if not visited[i] :
                q.append((i, count+1))
                visited[i] = True

    return -1

print(bfs(x))
    