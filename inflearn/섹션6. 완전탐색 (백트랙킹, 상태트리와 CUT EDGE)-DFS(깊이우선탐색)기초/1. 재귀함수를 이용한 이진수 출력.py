import sys

def dfs(x):
    if x == 0:
        return
    else:
        dfs(x//2)
        print(x % 2, end="") # 거꾸로 출력, 7라인 까지했다고 기록하고 스택이니까~

n = int(sys.stdin.readline())
dfs(n)
