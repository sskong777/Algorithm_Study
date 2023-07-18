'''
문제 특이사항 : 동전의 가지 수 k가 100가지이면 dfs로 못품
냅색 다이나믹으로 해결해야 함 (백준에서는 100가지로 되어있음)

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
