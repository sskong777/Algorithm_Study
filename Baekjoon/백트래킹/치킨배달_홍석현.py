# DFS 풀이법
import sys
input = sys.stdin.readline

def get_chicken_distance(homes, chickens):
    distance = 0
    for hx, hy in homes:
        chicken_distance = float('inf')
        for cx, cy in chickens:
            distance_temp = abs(hx - cx) + abs(hy - cy)
            if distance_temp < chicken_distance:
                chicken_distance = distance_temp
        distance += chicken_distance
    return distance


def dfs(chicken_idx, start_idx):
    global min_distance

    if len(selected_chickens) == M:
        distance = get_chicken_distance(homes, selected_chickens)
        min_distance = min(min_distance, distance)
        return

    for i in range(start_idx, len(chicken)):
        selected_chickens.append(chicken[i])
        dfs(chicken_idx + 1, i + 1)
        selected_chickens.pop()


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
homes = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            homes.append((i, j))

selected_chickens = []

min_distance = 1000000
dfs(0, 0)

# 결과 출력
print(min_distance)

# Combination 풀이법

# from itertools import combinations
#
# N,M = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# # print(arr)
# chick = []
# house = []
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 1:
#             house.append((i,j))
#         if arr[i][j] == 2:
#             chick.append((i,j))
#
# comb = list(combinations(chick,M))
# # print(comb)
#
# result = 999999
# # 치킨거리의 최솟값 구하기
# for com in comb:
#     temp = 0
#     for hi,hj in house:
#         distance = 10000
#         for si,sj in com:
#             distance = min(distance,abs(hi-si)+ abs(hj-sj))
#         temp += distance
#     result = min(result,temp)
#
# print(result)