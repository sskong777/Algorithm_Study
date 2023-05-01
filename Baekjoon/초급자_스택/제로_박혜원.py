# [10773] 제로

import sys

n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        n_list.append(num)
    else:
        n_list.pop()

print(sum(n_list))


"""
시간초과 - input() 대신  sys.stdin.readline()을 사용 

n = int(input())
n_list = []
for i in range(n):
    num = int(input())
    if num != 0:
        n_list.append(num)
    else:
        n_list.pop()

print(sum(n_list))
"""
