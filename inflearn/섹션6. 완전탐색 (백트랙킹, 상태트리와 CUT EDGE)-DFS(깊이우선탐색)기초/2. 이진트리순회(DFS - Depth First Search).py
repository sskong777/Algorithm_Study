'''
      1
   2     3   <- dfs(v*2), dfs(v*2 + 1)
4   5  6   7

전위순회 출력 : 1 2 4 5 3 6 7
중위순회 출력 : 4 2 5 1 6 3 7
후위순회 출력 : 4 5 2 6 7 3 1

'''

import sys

def dfs(v):
    if v > 7:
        return
    else:
        # print(v, end=" ") # 전위순회, 호출 넘어가기 전에 값을 찍음, 대부분의 문제
        dfs(v*2)
        # print(v, end=" ") # 중위순회, 왼쪽 먼저 다 처리하고 오른쪽으로 가니까, 거의 안쓰임
        dfs(v*2 + 1)
        print(v, end=" ") # 후위순회, 왼쪽/오른쪽 다 하고 자기 자신 처리할 때, 병합 정렬이 대표적


n = int(sys.stdin.readline())
dfs(1)