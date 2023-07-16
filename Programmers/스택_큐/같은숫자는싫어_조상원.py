from collections import deque
def solution(arr):
    ret = []
    d = deque(arr)
    while d:
        t = d.popleft()

        if not ret:
            ret.append(t)
        else:
            if ret[-1] != t:
                ret.append(t)

    return ret