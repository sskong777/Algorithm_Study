import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
a_arr = list(map(int, input().strip().split()))
b_arr = list(map(int, input().strip().split()))

answer = a_arr + b_arr
answer.sort()

print(*answer)