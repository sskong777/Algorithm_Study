'''
input
5 20
10 5
25 12
15 8
6 3
7 4

output
41
'''

import sys

def dfs(v, points, times):
    global result
    if times > m:
        return
    if v == n:
        if points > result:
            result = points
    else:
        # for문 쓸 필요 없었음
        dfs(v + 1, points + problems[v][0], times + problems[v][1])
        dfs(v + 1, points, times)

input = sys.stdin.readline
n, m = map(int, input().split())
problems =[]
for _ in range(n):
    problem = list(map(int, input().split()))
    problems.append(problem)

problems.sort(key= lambda x : (-x[0], x[1]))
result = 0
dfs(0, 0, 0)
print(result)