from collections import deque
def solution(people, limit):
    answer = 0
    d = deque(sorted(people))
    
    boat = 0
    cnt = 0
    while d:
        if d[0] + d[-1] > limit:
            d.pop()
        else:
            d.pop()
            if d:
                d.popleft()
        cnt += 1
    
    return cnt