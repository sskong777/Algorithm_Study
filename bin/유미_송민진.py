# # 시도 1
# import sys
# import math
# input = sys.stdin.readline
#
# p_dict = {}
# now_x, now_y = map(int, input().strip().split())
# for _ in range(3):
#     per_x, per_y = map(int, input().strip().split())
#     p_dict[(per_x, per_y)] = False
#
# answer = 0
# while True:
#     people = list(p_dict.keys())
#     visited = list(p_dict.values())
#     if False not in visited:
#         break
#
#     min_d = int(1e9)
#     tmp = ()
#     for x, y in people:
#         if p_dict[(x, y)] == False:
#             if min_d > ((now_x - x)**2 + (abs(now_y - y))**2)**(1/2):
#                 min_d = abs(now_x - x) + abs(now_y - y)
#                 tmp = (x, y)
#     p_dict[tmp] = True
#     answer += min_d
#     now_x, now_y = tmp
#
# print(math.floor(answer))

# 시도 2 - 수동 완전 탐색
import sys
import math
input = sys.stdin.readline
INF = int(1e9)

nodes = [tuple(map(int, input().strip().split()))]
for _ in range(3):
    nodes.append(tuple(map(int, input().strip().split())))

distance = [[INF] * 4 for _ in range(4)]
for a in range(4):
    for b in range(4):
        distance[a][b] = (abs(nodes[a][0] - nodes[b][0])**2 + (abs(nodes[a][1] - nodes[b][1]))**2)**(1/2)

min_d = INF
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i != j and j != k and i != k:
                d = distance[0][i] + distance[i][j] + distance[j][k]
                min_d = min(min_d, d)

print(math.floor(min_d))