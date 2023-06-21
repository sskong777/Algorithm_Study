import heapq 
import sys

n = int(sys.stdin.readline().rstrip())
heap = []

for i in range(n):
    info = int(sys.stdin.readline().rstrip())
    
    if info == 0 :
        if heap :
            print(heapq.heappop(heap)) 
        else:
            print(0)
    else:
        heapq.heappush(heap,info) 