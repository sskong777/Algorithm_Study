'''
input
5
3
6
0
5
0
2
4
0
-1

output
3
5
2
'''

import sys
import heapq as hq
input = sys.stdin.readline

nums = [] # 리스트가 필요, heappush랑 heappop하면 heap으 로 작동
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(nums) == 0:
            print(-1)
        else:
            print(hq.heappop(nums))
    else:
        hq.heappush(nums, n)
