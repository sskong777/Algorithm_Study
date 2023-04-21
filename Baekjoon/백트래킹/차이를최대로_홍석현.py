N = int(input())
arr = list(map(int,input().split()))

def calc(arr):
    ans = 0
    for i in range(N-1):
        ans += abs(arr[i]-arr[i+1])
    return ans

answer = 0
def dfs(depth):
    global answer
    if depth == N:
        answer = max(answer,calc(arr))
        return

    for i in range(depth, N):
        arr[depth], arr[i] = arr[i], arr[depth]
        dfs(depth+1)
        arr[depth], arr[i] = arr[i], arr[depth]

dfs(0)
print(answer)