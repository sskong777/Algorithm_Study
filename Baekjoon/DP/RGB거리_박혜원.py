# [1149] RGB거리

# 입력 받기
num = int(input())
# costs = [list(map(int, input().split())) for _ in range(num)]
costs = []
for i in range(num):
    rgb_costs = list(map(int, input().split()))
    costs.append(rgb_costs)


def dp(num, costs):
    # N x 3 크기의 2차원 배열 만들기
    dp = [[0] * 3 for _ in range(num)]

    for i in range(num):
        for j in range(3):
            if i == 0:
                dp[i][j] = costs[i][j]
            else:
                dp[i][j] = costs[i][j] + \
                    min(dp[i-1][(j+1) % 3], dp[i-1][(j+2) % 3])
    # 배열의 인덱스가 0부터 시작하니까 마지막인 num번째 집을 [num-1]라고 표현
    return min(dp[num-1])


# 출력
print(dp(num, costs))


"""
# 다른 방법
dp = [[0]*3 for _ in range(num)]

dp[0][0], dp[0][1], dp[0][2] = colors[0][0], colors[0][1], colors[0][2]
for i in range(1, num):  # 마지막에서 앞 집 까지
    dp[i][0] = min(dp[i-1][1]+colors[i][0], dp[i-1][2]+colors[i][0])
    dp[i][1] = min(dp[i-1][0]+colors[i][1], dp[i-1][2]+colors[i][1])
    dp[i][2] = min(dp[i-1][0]+colors[i][2], dp[i-1][1]+colors[i][2])
    
print(min(dp[num-1]))
"""
