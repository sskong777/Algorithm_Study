import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) # 재귀허용 깊이 늘려주는 코드 *필수*

def dfs(b:list[list[str]], v:list[list[bool]], i:int, j:int, estate:int, n:int) -> bool:
    global count
    if b[i][j] == '0' or v[i][j] == True:
        return
    
    v[i][j] = True
    b[i][j] = estate
    count += 1
    # 상, 우, 하, 좌
    x, y = i, j
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for p in range(4):
        x = i + dx[p]
        y = j + dy[p]
        if x < 0 or x >= n or y < 0 or y >= n:
            continue
        dfs(b, v, x, y, estate, n)
    
    

n = int(input())
count = 0
estate = 1
board = []
visited = [[False]*n for _ in range(n)]
answer = []
for _ in range(n):
    board.append(list(input().strip()))

for i in range(n):
    for j in range(n):
        if board[i][j] == '1' and visited[i][j] == False:
            dfs(board, visited, i, j, estate, n)
            answer.append(count)
            estate += 1
            count = 0

answer.sort()
print(estate-1)
for i in range(len(answer)):
    print(answer[i])