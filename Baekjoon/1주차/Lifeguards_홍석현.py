from itertools import combinations

N = int(input())

arr = []
for _ in range(N):
    start, end = map(int,input().split())
    arr.append((start,end))

ans = 0
arr_combi = combinations(arr,N-1)


for i in arr_combi:
    time = []
    for j in i:
        time += [k for k in range(j[0], j[1])]
    ans = max(ans,len(set(time)))
# for i in arr_combi:
#     time = [j for j in range(i[0][0], i[0][1])] + [k for k in range(i[1][0], i[1][1])]
#     # print(time)
#     ans = max(ans,len(set(time)))
#
#
print(ans)