'''
input
5 3
2 4 5 8 12
6

output
2
'''
import sys

def dfs(L, total, check):
    global cnt
    if L == n:
        if check == k:
            if total % m == 0:
                cnt += 1
    else:
        dfs(L + 1, total + nums[L], check + 1)
        dfs(L + 1, total, check)


input = sys.stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))
m = int(input())
cnt = 0

dfs(0, 0, 0)

print(cnt)