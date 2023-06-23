import sys

n, m = map(int, sys.stdin.readline().split())
pocketmons_int = {}
pocketmons_str = {}

for i in range(n):
    po = sys.stdin.readline().strip()
    pocketmons_int[i] = po
    pocketmons_str[po] = i

for _ in range(m):
    p = sys.stdin.readline().strip()
    if p.isdigit():
        print(pocketmons_int[int(p)-1])
    else:
        print(pocketmons_str[p] + 1)