from itertools import combinations

n, m = map(int, input().split())
board = []
chicken = []
home = []

for i in range(n):
    board.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((i+1, j+1))
        elif board[i][j] == 1:
            home.append((i+1, j+1))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    tot = 0
    for hx, hy in home:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        tot += temp
    
    return tot
    
    
res = 1e9

for candidate in candidates:
    res = min(res, get_sum(candidate))

print(res)