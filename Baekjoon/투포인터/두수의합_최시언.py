#조합을 만드는 것이 파이썬에는 존재한다!
#근데 타임아웃인데요

import sys

n = int(input())
number_array = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

answer = 0
left, right = 0, n-1 # 왼쪽, 오른쪽
while left < right:
    temp = number_array[left] + number_array[right]
    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(answer)
