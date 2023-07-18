'''
1 ~ n까지 번호가 적힌 구슬
중복을 허락하여 m번을 뽑아 일렬로 나열
3 <= n <= 10
2 <= m <= n
'''

import sys
def dfs(L):
    global cnt
    if L == m:
        print(*res)
        cnt += 1
    else:
        for i in range(1, n+1):
            res[L] = i # m이 2이면 res = [ , ]라고 생각
            dfs(L+1)


n, m = map(int, sys.stdin.readline().split())
res = [0] * m
cnt = 0
dfs(0)
print(cnt)