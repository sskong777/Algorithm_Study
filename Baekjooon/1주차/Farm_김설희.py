# x + y = n
# ax + b(n-x) = w

A, B, N, W = map(int, input().split())
ans = False
cnt = 0

for x in range(1, 1001):
  if A*x + B*(N-x) == W:
    if N-x > 0:
      ans = True
      cnt += 1
      sheep = x


print(-1) if ans == False or cnt > 1 else print(sheep, N-sheep)
