n, m = map(int, input().split())

cube = list()
ans = 0

for idx in range(m):
     cube.append(list(map(int, input().split())))

for idx in range(m):
    i, j, k = cube[idx]

    if ([i+1, j, k] in cube) and ([i, j+1, k] in cube) and ([i, j, k+1] in cube) and ([i-1, j, k] in cube) and ([i, j-1, k] in cube) and ([i, j, k-1] in cube):
        ans +=1

print(ans)
