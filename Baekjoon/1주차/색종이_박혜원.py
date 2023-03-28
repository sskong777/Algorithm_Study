# [2563] 색종이

matrix = []    # 영배열의 100*100 빈도화지 생성
for _ in range(101):
    temp = []
    for _ in range(101):
        temp.append(0)
    matrix.append(temp)
# for line in matrix:
#     print(line)

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    for _x in range(x, x+10):
        for _y in range(y, y+10):
            matrix[_x][_y] = 1   # 이중배열, 색칠 되는 부분 -> 1

total = 0
for line in matrix:
    total += sum(line)

print(total)
