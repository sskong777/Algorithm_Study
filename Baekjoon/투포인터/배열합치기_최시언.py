#배열 합치기~!

import sys

read = lambda: sys.stdin.readline().rstrip()

N, M = map(int, read().split())
num_list_N = list(map(int, read().split()))
num_list_M = list(map(int, read().split()))

answer = num_list_N + num_list_M
answer.sort()
print(*answer)
