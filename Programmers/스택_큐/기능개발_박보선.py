from collections import deque

def solution(progresses, speeds):
    answer = []
    count = 0
    
    p = deque(progresses)
    s = deque(speeds)
    
    while p:
        a = 100 - p[0]
        q = a // s[0]
        r = a % s[0]
        if r > 0:
            q += 1
        
        for i in range(len(p)):
            p[i] += s[i] * q

        while p:
            if p[0] < 100:
                break
            count += 1
            p.popleft()
            s.popleft()
        answer.append(count)
        count = 0
    
    return answer