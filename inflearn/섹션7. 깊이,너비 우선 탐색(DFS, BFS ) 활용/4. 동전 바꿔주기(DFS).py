'''
input
20
3
5 3
10 2
1 5

output
4
'''
import sys

def dfs(L, total):
    global cnt
    if total > T:
        return
    if L == k:
        if total == T:
            cnt += 1
    else:
        for i in range(ni[L] + 1):
            dfs(L + 1, total + pi[L]*i)

input = sys.stdin.readline
T = int(input())
k = int(input())
pi = []
ni = []
for _ in range(k):
    p, n = map(int, input().split())
    pi.append(p)
    ni.append(n)

cnt = 0
dfs(0, 0)
print(cnt)
