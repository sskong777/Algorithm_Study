N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(M)]
count = 0
for i,j,k in arr:
    if [i+1,j,k] in arr and [i-1,j,k] in arr and [i,j+1,k] in arr and [i,j-1,k] in arr and [i,j,k+1] in arr and [i,j,k-1] in arr:
        count += 1

print(count)