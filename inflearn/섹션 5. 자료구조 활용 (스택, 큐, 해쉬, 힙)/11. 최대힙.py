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
6
5
5
'''

# 최대힙은 부호를 바꾸면 됨

import sys
import heapq as hq
input = sys.stdin.readline

nums = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(nums) == 0:
            print(-1)
        else:
            print(-hq.heappop(nums))
    else:
        hq.heappush(nums, -n)
