# [15649] N과M1

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
check = [False] * (N+1)


def backtracking(num):   # 재귀함수 정의
    if num == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if check[i] == False:
            check[i] = True
            result.append(i)
            backtracking(num+1)
            check[i] = False
            result.pop()


backtracking(0)  # 0 부터 시작
