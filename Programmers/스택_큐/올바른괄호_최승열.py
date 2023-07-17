from collections import deque
def solution(s):
    dq = deque()
    for c in s:
        if dq and dq[-1] == '(' and c == ')': dq.pop()
        else: dq.append(c)
    return len(dq) == 0