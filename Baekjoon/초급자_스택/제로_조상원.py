import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

s=[]
for i in arr:
    if i == 0:
        s.pop()
    else:
        s.append(i)
print(sum(s))