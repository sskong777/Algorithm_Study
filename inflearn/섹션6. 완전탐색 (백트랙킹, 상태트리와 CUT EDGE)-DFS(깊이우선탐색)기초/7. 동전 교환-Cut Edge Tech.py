'''
거스름돈을 가장 적은 수의 동전으로 교환
종류 개수: 1 <= n <= 12
거슬러 줄 금액: 1 <= m <= 500

input
3
1 2 5
15

output
3

레벨이 동전 사용 개수
'''

import sys

def dfs(L, total):
    global result
    if L > result:  # 시간 초과 나므로 추가, 개수 적은게 나왔는데 더 알아볼 필요가 없음!
        return
    if total > m:
        return
    if total == m:
        result = min(result, L)
    else:
        for i in range(n):
            if total + coin_kinds[i] > m:
                break
            dfs(L+1, total + coin_kinds[i])

input = sys.stdin.readline
n = int(input())
coin_kinds = list(map(int, input().split()))
m = int(input())

coin_kinds.sort(reverse=True) # 가장 큰 동전부터 하도록 정렬
result = float('inf') # 큰값을 result = float('inf') 이렇게 표현할 수도 있다.

dfs(0, 0)

print(result)