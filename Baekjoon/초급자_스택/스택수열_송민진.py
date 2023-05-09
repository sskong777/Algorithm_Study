import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
answer = deque([])
stack = []
tmp = []
for _ in range(n):
    answer.append(int(input()))

def s_push(num):
    stack.append(num)

def s_pop():
    popped = stack.pop()
    if answer[0] == popped:
        answer.popleft()
    else:
        return False

def solution():
    for i in range(1,n+1):
        if stack:
            while stack and stack[-1] == answer[0]:
                if s_pop() != False:
                    tmp.append("-")
            else:
                s_push(i)
                tmp.append("+")
        else:
            s_push(i)
            tmp.append("+")

    while stack:
        if s_pop() == False:
            return False
        else:
            tmp.append("-")


if solution() == False:
    print("NO")
else:
    for t in tmp:
        print(t)