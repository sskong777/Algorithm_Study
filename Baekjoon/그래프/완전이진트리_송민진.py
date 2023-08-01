import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
answer = [[] for _ in range(k)]
visits = list(map(int, input().strip().split()))
q = deque([])
q.append((visits, 0))

while q:
    arr, depth = q.popleft()
    mid = len(arr)//2
    answer[depth].append(arr[mid])
    if len(arr) != 1:
        q.append((arr[:mid], depth+1))
        q.append((arr[mid+1:], depth+1))

for ans in answer:
    print(*ans)