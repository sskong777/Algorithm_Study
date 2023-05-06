import sys

k = int(sys.stdin.readline())
stack = []

for _ in range(k):
    n = int(sys.stdin.readline())
    stack.pop() if n == 0 else stack.append(n)

print(sum(stack)) if len(stack) != 0 else print(0)