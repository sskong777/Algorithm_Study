import sys
import math
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
answer = 0
n=1000
a = [False,False] + [True]*(n-1)

for i in range(2,n+1):
  if a[i]:
    for j in range(2*i, n+1, i):
        a[j] = False

for num in nums:
    if a[num]:
        answer += 1

print(answer)