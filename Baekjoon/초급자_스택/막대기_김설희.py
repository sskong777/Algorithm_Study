import sys

n = int(sys.stdin.readline())

cnt =  0
stack = [int(sys.stdin.readline()) for _ in range(n)]

tmp = 0

for i in stack[::-1]:
    if tmp < i:
        tmp = i
        cnt += 1

print(cnt)

