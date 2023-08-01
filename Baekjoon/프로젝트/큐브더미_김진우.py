N, M = map(int, input().split())

# 큐브의 위치를 저장할 3차원 배열 생성
cubes = [[[False] * (N + 2) for _ in range(N + 2)] for _ in range(N + 2)]

# 입력으로 주어진 큐브의 위치를 True로 설정
for _ in range(M):
    i, j, k = map(int, input().split())
    cubes[i][j][k] = True

count = 0

# 모든 좌표에 대해 검사
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if cubes[i][j][k]:
                # 주변 좌표 검사
                if cubes[i + 1][j][k] and cubes[i - 1][j][k] and cubes[i][j + 1][k] and \
                        cubes[i][j - 1][k] and cubes[i][j][k + 1] and cubes[i][j][k - 1]:
                    count += 1

print(count)
