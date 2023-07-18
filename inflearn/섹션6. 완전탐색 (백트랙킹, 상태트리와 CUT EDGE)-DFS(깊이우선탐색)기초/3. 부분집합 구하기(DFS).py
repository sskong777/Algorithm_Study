'''
각 원소를 사용한다 / 사용하지 않는다.

input이 3이면 output이 다음과 같음
1 2 3
1 2
1 3
1
2 3
2
3
'''

import sys
def dfs(v):
    if v == n + 1:
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end=" ")
        print()
    else:
        check[v] = 1 # 사용한다
        dfs(v+1)
        check[v] = 0 # 사용하지 않는다
        dfs(v+1)


n = int(sys.stdin.readline())
check = [0] * (n + 1) # 원소 사용한다/안한다에 대한 체크 필요하므로
dfs(1)