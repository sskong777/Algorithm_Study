import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))

answer = arr[0]
tmp = arr[0]
del arr[0]

for now in arr:
    if now != tmp + 1:
        answer += now
    tmp = now

print(answer)