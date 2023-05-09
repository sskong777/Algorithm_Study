import sys
input = sys.stdin.readline

n = int(input())
coms = [[0] for _ in range(n)] * (n+1)
virus = [False] * (n+1)

conns = int(input())
for _ in range(conns):
    com1, com2 = map(int, input().strip().split())
    coms[com1].append(com2)
    coms[com2].append(com1)

def dfs(idx):
    if idx != 0 and virus[idx]:
        for node in coms[idx]:
            if not virus[node]:
                virus[node] = True
                dfs(node)

virus[1] = True
dfs(1)

print(virus[2:].count(True))