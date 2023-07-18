'''
input
3
1 5 7

output
2
'''
import sys

def dfs(L, total):
    if total > 0:
        result.add(total)
    if L == k:
        return

    else:
        dfs(L + 1, total + weights[L])
        dfs(L + 1, total - weights[L])
        dfs(L + 1, total)


input = sys.stdin.readline
k = int(input())
weights = list(map(int, input().split()))
S = sum(weights)
result = set()

dfs(0, 0)

print(S-len(result))