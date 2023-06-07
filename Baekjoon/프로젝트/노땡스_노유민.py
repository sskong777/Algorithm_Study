import sys

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

count = li[0]
for i in range(1, len(li)):
    if li[i-1]+1 != li[i]:
        count += li[i]

print(count)
