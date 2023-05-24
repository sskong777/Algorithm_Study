# 행 n, 열 m
n, m = map(int, input().split())
room = []
visited = [[0]*m for _ in range(n)]

for i in range(n):
    room.append(list(input()))

cnt = 0
for i in range(n):
    a = ''
    for j in range(m):
        if room[i][j] == '-':
            if room[i][j] != a:
                cnt += 1
        a = room[i][j]

for j in range(m):
    a = ''
    for i in range(n):
        if room[i][j] == '|':
            if room[i][j] != a:
                cnt += 1
        a = room[i][j]

print(cnt)