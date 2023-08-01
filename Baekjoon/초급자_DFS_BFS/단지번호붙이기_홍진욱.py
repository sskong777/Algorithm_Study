def dfs(row, col):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited[row][col] = True

    count = 1

    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]

        if 0 <= next_row < N and 0 <= next_col < N and not visited[next_row][next_col] and map[next_row][next_col] == '1':
            count += dfs(next_row, next_col)

    return count

N = int(input())
map = [input() for _ in range(N)]
visited = [[False] * N for _ in range(N)]

complexes = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and map[i][j] == '1':
            count = dfs(i, j)
            complexes.append(count)

complexes.sort()

print(len(complexes))
for count in complexes:
    print(count) 
