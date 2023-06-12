import sys

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

count = 1
for i in range(1, len(li)):
    if li[i-1] <= li[i]:
        count += 1

print(count)
