from collections import deque

def solution(arr):
    answer = []
    stack = deque()

    tmp = -1
    for a in arr:

        if stack:
            tmp = stack.pop()

        if tmp == a:
            stack.append(a)

        else:
            stack.append(a)
            answer.append(a)

    return answer