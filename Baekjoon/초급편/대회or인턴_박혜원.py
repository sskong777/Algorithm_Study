# [2875] 대회or인턴
N, M, K = map(int, input().split())


count = 0
while True:
    N -= 2
    M -= 1
    if N < 0 or M < 0 or (N + M) < K:
        break
    count += 1
print(count)
