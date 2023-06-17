import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

can = False
result = 0
length = -1

for i in range(n - 1):
    start = li[i]
    end = li[i + 1]
    if end - start > length:
        for j in range(start + 1, end):
            if j - start > length and end - j > length:
                length = j - start
                result = j
                can = True

if can:
    print(result)
else:
    print(-1)
