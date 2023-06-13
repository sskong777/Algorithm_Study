# [27982] 큐브더미

N, M = map(int, input().split())
answer = 0
# 큐브를 저장하는 3차원 배열 초기화
cubes = [[[0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]

# 큐브좌표 입력 받기
for _ in range(M):
    i, j, k = map(int, input().split())
    cubes[i][j][k] = 1


# 모든 큐브에 대해 조건 확인
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if cubes[i][j][k] == 1:
                # 이웃좌표확인
                neighbors = [(i+1, j, k), (i-1, j, k), (i, j+1, k),
                             (i, j-1, k), (i, j, k+1), (i, j, k-1)]
                for x, y, z in neighbors:
                    # 이웃 좌표 중 하나라도 큐브가 존재하지 않으면 조건 불만족
                    if x < 1 or x > N or y < 1 or y > N or z < 1 or z > N or cubes[x][y][z] == 0:
                        break
                else:
                    # 모든 이웃 좌표에 큐브가 존재하면 조건 만족
                    answer += 1

print(answer)
