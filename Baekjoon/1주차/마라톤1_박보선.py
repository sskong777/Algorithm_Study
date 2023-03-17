import sys
input = sys.stdin.readline

dis = [0, ]
pos = []
answer = 0
n = int(input())
x, y = map(int, input().split())
pos.append([x, y])

for i in range(1, n):
    x, y = map(int, input().split())
    pos.append([x, y])
    
    dis.append(abs(pos[i-1][0] - pos[i][0]) + abs(pos[i-1][1] - pos[i][1]))

total = sum(dis)
answer = 2000 * 100000

for i in range(1, n-1):
    temp = total - (dis[i] + dis[i + 1]) + (abs(pos[i-1][0] - pos[i+1][0]) + abs(pos[i-1][1] - pos[i+1][1]))
    answer = min(answer, temp)
print(answer)