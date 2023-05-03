import sys

n = int(input())
stack = []
temp = 0

for i in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        stack.pop()
    else:
        stack.append(temp)

print(sum(stack))
    
