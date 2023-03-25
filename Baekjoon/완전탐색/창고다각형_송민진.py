n = int(input())
columns = []
answer = 0
for _ in range(n):
    columns.append(tuple(map(int, input().split())))

columns.sort()

start_l, start_h = columns[0]
last_l, last_h = columns[-1][0], columns[-1][1]
max_l, max_h = max(columns, key=lambda x:x[1])

now_h = start_h
for l in range(start_l, max_l):
    for column in columns:
        if l == column[0]:
            now_h = max(now_h, column[1])
    answer += now_h

answer += max_h

now_h = last_h
for l in range(last_l, max_l, -1):
    for column in columns:
        if l == column[0]:
            now_h = max(now_h, column[1])
    answer += now_h

print(answer)