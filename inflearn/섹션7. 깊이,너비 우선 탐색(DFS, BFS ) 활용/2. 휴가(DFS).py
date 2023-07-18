'''
t : 상담을 완료하는 데 걸리는 기간
p : 상담을 했을 때 받을 수 있는 금액

input
7
3 40
2 15
3 50
3 25
2 20
2 30
1 10

output
80
'''

''' 
# 내가 푼 코드
import sys

# v가 몇 일차
def dfs(v, t, t_total, p_total):
    global result
    if v > n:
        return
    if v == n:
        if result < p_total:
            result = p_total
    else:
        dfs(v + ti[v], ti[v], t_total + ti[v], p_total + pi[v])
        dfs(v + 1, ti[v], t_total, p_total)


input = sys.stdin.readline
n = int(input())
ti = []
pi = []
for _ in range(n):
    t, p = map(int, input().split())
    ti.append(t)
    pi.append(p)

result = 0
dfs(0, 0, 0, 0)
print(result)
'''
import sys

def dfs(L, total):
    global result
    if L == n + 1:
        if total > result:
            result = total
    else:
        if L + ti[L] <= n + 1:
            dfs(L + ti[L], total + pi[L])
        dfs(L + 1, total)


input = sys.stdin.readline
n = int(input())
ti = list()
pi = list()
for _ in range(n):
    t, p = map(int, input().split())
    ti.append(t)
    pi.append(p)

result = 0
# index를 문제 수로 하기 위해서 0을 집어넣어서 뒤로 미룬다
ti.insert(0, 0)
pi.insert(0, 0)

dfs(1, 0)

print(result)