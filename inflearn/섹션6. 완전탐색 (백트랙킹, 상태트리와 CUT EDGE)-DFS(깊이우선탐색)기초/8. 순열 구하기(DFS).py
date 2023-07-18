'''
1 ~ n까지 번호가 적힌 구슬
m개를 뽑아 일렬로 나열
3 <= n <= 10
2 <= m <= n
'''
import sys

def dfs(v):
    global cnt
    if v == m:
        print(*res)
        cnt += 1
    else:
        for i in range(1, n + 1):
            if check[i] == 0: # 그냥 순열은 중복되면 안되니까 체크를 해야함
                check[i] = 1
                res[v] = i
                dfs(v + 1) # 여기서 호출

                check[i] = 0 # 되돌아오는거임, 다시 초기화

input = sys.stdin.readline
n, m = map(int, input().split())

res = [0] * m
check = [0] * (n + 1)
cnt = 0

dfs(0)

print(cnt)
