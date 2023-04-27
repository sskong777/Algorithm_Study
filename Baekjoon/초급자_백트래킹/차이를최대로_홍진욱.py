def dfs(cnt):
    global ans
    if cnt == n:
        sum = 0
        for i in range(n-1):
            sum += abs(arr[order[i]] - arr[order[i+1]])
        ans = max(ans, sum)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        order[cnt] = i
        dfs(cnt+1)
        visited[i] = False

n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n
order = [0] * n
ans = 0

dfs(0)
print(ans)
