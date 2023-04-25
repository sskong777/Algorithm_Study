import sys
input = sys.stdin.readline

def Knapsack(count, maxWeight, knapsack):
    dp = [[0] * (maxWeight + 1) for _ in range(count + 1)]

    for i in range(count + 1):
        for j in range(maxWeight + 1):
            if i == 0 & j == 0:
                dp[i][j] = 0
            elif (j - knapsack[i - 1][0] >= 0) & (knapsack[i - 1][0] <= maxWeight):
                dp[i][j] = max(knapsack[i - 1][1] + dp[i - 1][j - knapsack[i - 1][0]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[count][maxWeight]

count, maxWeight = map(int, input().split())

knapsack = []

for i in range(count):
    w, v = map(int, input().split())
    knapsack.append([w, v])

print(Knapsack(count, maxWeight, knapsack))