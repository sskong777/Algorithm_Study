# [12865] 평범한배낭
"""
 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 출력하자!
"""
N, K = map(int, input().split())  # 물품의 수(N), 버틸수 있는 무게(K)

W = [0] * (N+1)
V = [0] * (N+1)
# 각 물건의 무게(W), 가치(V)
for i in range(1, N+1):
    W[i], V[i] = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]


for i in range(1, N+1):
    for j in range(1, K+1):
        if j - W[i] >= 0:
            # max(i 번째 물건을 선택하지 않은 경우, i 번째 물건을 선택한 경우)
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]]+V[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
