import sys
from collections import deque

N, M = map(int, input().split())
L = sys.stdin.readlines()

orders = {}
cnt = [0]*N

for i in range(N):
    for a in map(int, L[i].strip().split()[1:]):
        orders.setdefault(a, deque()).append(i)

for s in map(int, L[-1].split()):
    if s not in orders or not orders[s]: continue
    cnt[orders[s].popleft()] += 1

print(*cnt)