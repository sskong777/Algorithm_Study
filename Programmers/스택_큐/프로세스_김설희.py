from collections import deque


def solution(priorities, location):
    execute = 0  # 실행했다!

    dq = deque([(i, p) for i, p in enumerate(priorities)])

    while dq:
        if dq[0][1] < max([p[1] for p in dq]):
            dq.append(dq.popleft())
        else:
            if dq[0][0] == location:
                execute += 1
                return execute
                break
            else:
                execute += 1
                dq.popleft()