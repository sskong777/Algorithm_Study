A, B, C, N = map(int, input().split())
ans = False
# N = Ax + By + Cz
for i in range(0, 51):
  for j in range(i, 51):
    for k in range(j, 51):
      if A*i + B*j + C*k == N:
        print(1)
        ans = True
        break
if ans == False:
  print(0)
