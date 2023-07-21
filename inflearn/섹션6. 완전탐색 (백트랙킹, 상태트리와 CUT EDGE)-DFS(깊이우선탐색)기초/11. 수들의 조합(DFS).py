'''
input
5 3
2 4 5 8 12
6

output
2
'''

# 내가 푼 정답 풀이
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
'''

# 다른 풀이 (강의 풀이) - 받는 건 똑같은데 구현을 다르게 함
import sys

def dfs(L, s, total):
    global cnt
    if L == k:
        if total % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            dfs(L+1, i+1, total + nums[i])

input = sys.stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))
m = int(input())
cnt = 0

dfs(0, 0, 0)

print(cnt)