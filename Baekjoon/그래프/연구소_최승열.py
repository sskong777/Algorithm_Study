from itertools import combinations

f = lambda:map(int, input().split())
g = lambda n:((r,c) for c in range(C) for r in range(R) if M[r][c] == n)

R, C = f()
M = [list(f()) for _ in range(R)]

V = list(g(2))

vector = [(0,1), (1,0), (0,-1), (-1,0)]

def spread(r, c, l):
    for dr, dc in vector:
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and l[nr][nc] == 0:
            l[nr][nc] = 2
            spread(nr, nc, l)

def copyOfM():
    return [[M[r][c] for c in range(C)] for r in range(R)]

ans = 0
for cand in combinations(list(g(0)), 3):
    for r,c in cand: M[r][c] = 1
    l = copyOfM()
    for vr, vc in V:
        spread(vr, vc, l)
    ans = max(ans, sum(m.count(0) for m in l))
    for r,c in cand: M[r][c] = 0

print(ans)


