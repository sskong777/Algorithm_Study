import sys
input = sys.stdin.readline

n = int(input())
stack = []
highest = 0
cnt = 0
for _ in range(n):
    stack.append(int(input()))

for _ in range(n):
    now = stack.pop()
    if now > highest:
        highest = now
        cnt += 1

print(cnt)
