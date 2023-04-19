n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 M개를 고른 수열 (중복 가능, 같은 수 여러번 골라도 됨)
# 고른 수열은 비내림차순이어야함

numslist = []
def dfs(k):
    if len(numslist) == m:
        print(' '.join(map(str, numslist)))
        return

    for i in range(k, n+1):
        numslist.append(i)
        dfs(i)
        numslist.pop()

dfs(1)

