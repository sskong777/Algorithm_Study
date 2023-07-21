'''
두 개의 부분집합으로 나누었을 때 각각의 합이 같으면 YES
input
6
1 3 5 6 7 10

output
YES
'''


import sys
def dfs(L, sum):
    if sum > total // 2: # 시간 복잡도를 줄여주는 장치
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0) # 프로그램 자체를 종료시켜버림
    else:
        dfs(L+1, sum + numbers[L]) # 이 원소를 사용하겠다
        dfs(L+1, sum) # 안하겠다

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
total = sum(numbers)
dfs(0, 0)
print("NO")