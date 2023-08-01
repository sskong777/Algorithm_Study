N, M = map(int, input().split())
cubes = []
count = 0

for _ in range(M):
    cubes.append(list(map(int, input().split())))

for x, y, z in cubes:
    if [x + 1, y, z] in cubes and [x - 1, y, z] in cubes and [x, y + 1, z] in cubes and [x, y - 1, z] in cubes and [x, y, z + 1] in cubes and [x, y, z - 1] in cubes:
        count += 1

print(count)
