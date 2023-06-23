import heapq

import sys

input = sys.stdin.readline

n = int(input())

# arr = [int(input()) for _ in range(n)]
arr = []
heapq.heapify(arr)
ret = []
for _ in range(n):
    l = int(input())
    if l == 0:
        if not arr:
            ret.append(0)
        else:
            ret.append(heapq.heappop(arr))
    else:
        heapq.heappush(arr, l)

for i in ret:
    print(i)
