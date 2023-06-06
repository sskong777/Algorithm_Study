import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))

cnt = 1
for i in range(1, n):
    if arr[i-1] <= arr[i]:
        cnt += 1

print(cnt)