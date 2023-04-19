# permutation을 이용한 풀이

# from itertools import permutations
#
# N,M = map(int,input().split())
# arr = [i for i in range(1,N+1)]
# data = []
# data += permutations(arr,M)
# for i in data:
#     print(*i)


# dfs 백트래킹
def dfs(depth):

    if depth == M:
        print(" ".join(map(str,result)))
        return

    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = 1
            result[depth] = i
            dfs(depth+1)
            visited[i] = 0

N,M = map(int,input().split())
visited = [0] * (N+1)
result = [0] * M
dfs(0)