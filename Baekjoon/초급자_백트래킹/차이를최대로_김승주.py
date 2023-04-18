import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

ans = 0 
def back(depth):
    global ans

    if depth == n:
        tmp = sum(abs(explore[i]-explore[i+1]) for i in range(n-1))
        ans = max(ans, tmp)
        return
    
    for i in range(n):
        if not visited[i]:
            explore.append(nums[i])
            visited[i] = True
            back(depth+1)
            visited[i]= False
            explore.pop()

visited = [False]*n 
explore = []
back(0)
print(ans)