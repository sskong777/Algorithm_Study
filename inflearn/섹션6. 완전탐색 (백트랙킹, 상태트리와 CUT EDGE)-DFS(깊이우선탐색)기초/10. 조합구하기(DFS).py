'''
그냥 조합은 상태트리 구조가 좀 다르다
dfs(0, 1)부터~

input
4 2

output
1 2
1 3
1 4
2 3
2 4
3 4
6
'''

import sys

def dfs(L, total):
    global cnt
    if L == m:
        print(*result)
        cnt += 1
    else:
        for i in range(total, n + 1):
            result[L] = i
            print("dfs : ", L + 1, i + 1)
            dfs(L + 1, i + 1)
            print("dfs 이후임")

input = sys.stdin.readline
n, m = map(int, input().split()) # 4 2
result = [0] * m
cnt = 0

dfs(0, 1)
print(cnt)




