import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())

ret = [0] * n

d = defaultdict(deque)

for i  in range(n):
    c = list(map(int, input().split()))[1:]
    for l in c:
        d[l].append(i)

    
sl = list(map(int, input().split()))

k = d.keys()


for s in sl:
    if s in d.keys():
        if d[s]:
            i = d[s].popleft()
            ret[i] += 1
        

print(' '.join(list(map(str, ret))))
