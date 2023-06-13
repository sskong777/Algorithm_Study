N, M = map(int, input().split())
cubes = []

cnt = 0
for _ in range(M):
    cubes.append(list(map(int, input().split())))

for i, j, k in cubes:
    if [i+1, j, k] in cubes and [i-1, j, k] in cubes and [i, j+1, k] in cubes and [i, j-1, k] in cubes and [i, j, k+1] in cubes and [i, j, k-1] in cubes:
        cnt += 1


print(cnt)
