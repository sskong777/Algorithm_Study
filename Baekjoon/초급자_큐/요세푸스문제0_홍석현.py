from collections import deque

N, K = map(int,input().split())
result = []
q = deque([i for i in range(1,N+1)])

while q:
    for i in range(K-1):
        pass