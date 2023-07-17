from collections import deque

def solution(progresses, speeds):
    ret = []
    q = deque([])
    # 총 필요한 일수 계산
    for a, b in zip(progresses, speeds):
        l = 100 - a
        if l % b != 0:
            q.append(l // b + 1)
        else:
            q.append(l // b)
    
    print(q)
    prev = q.popleft()
    tmp = 1

    while q:
        c = q.popleft()
        # 전에 했던 작업 일수가 제일 많아서 같이 할 수 있으면
        if prev >= c:
            tmp += 1
        else:
            # 새로운 작업으로 바꿈
            prev = c
            ret.append(tmp)
            tmp = 1
    ret.append(tmp)
    return ret