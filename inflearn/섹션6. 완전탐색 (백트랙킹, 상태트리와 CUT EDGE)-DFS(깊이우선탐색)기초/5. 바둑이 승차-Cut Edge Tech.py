'''
input
259 5
81
58
42
33
61

output
242
'''

''' 시간 초과 나는 테스트 케이스가 있으므로 변수를 하나 더 설정한다.
def dfs(L, sum):
    global result
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        dfs(L+1, sum + dogs[L])
        dfs(L+1, sum)

import sys

c, n = map(int, sys.stdin.readline().split())
dogs = [0] * n
for i in range(n):
    dogs[i] = int(sys.stdin.readline())

result = -1 # 0이면 안된다. dfs(3, 0) 이런식이면 result가 갱신되지 않는다.
dfs(0, 0)
print(result)
'''

def dfs(L, sum, tsum): # 부분집합에 상관없이 판단한 것들은 tsum으로
    global result
    if sum + (total-tsum) < result: # 시간복잡도를 줄이기 위해서
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        dfs(L+1, sum + dogs[L], tsum + dogs[L])
        dfs(L+1, sum, tsum + dogs[L])

import sys

c, n = map(int, sys.stdin.readline().split())

dogs = [0] * n
for i in range(n):
    dogs[i] = int(sys.stdin.readline())

total = sum(dogs)
result = -1 # 0이면 안된다. dfs(3, 0) 이런식이면 result가 갱신되지 않는다.

dfs(0, 0, 0)
print(result)
