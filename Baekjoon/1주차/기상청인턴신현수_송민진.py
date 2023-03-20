n, k = map(int, input().split())
temps = list(map(int, input().split()))

answer = sum(temps[:k])
for i in range(1, n-k+1):
    answer = max(answer, sum(temps[i:i+k]))

print(answer)