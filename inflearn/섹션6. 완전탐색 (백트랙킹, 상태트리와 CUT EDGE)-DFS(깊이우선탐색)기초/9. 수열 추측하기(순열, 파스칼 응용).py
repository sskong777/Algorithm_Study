'''
파스칼 삼각형
이항계수

다시 복습할 것
'''

import sys

def dfs(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end = ' ')
        sys.exit(0) # 프로그램 전체 종료
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                dfs(L+1, sum + (p[L]*b[L]))
                ch[i] = 0

input = sys.stdin.readline
n, f = map(int, input().split())
p = [0] * n
b = [1] * n
ch = [0] * (n + 1)
for i in range(1, n):
      b[i] = b[i-1] * (n-i) // i
# for x in b: # 이항계수가 제대로 잘 찍히는지 확인
#     print(x, end = ' ')
dfs(0, 0)