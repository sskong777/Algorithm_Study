from collections import deque
def solution(priorities, location):
    answer = 1
    dq = deque(priorities)
    while answer < len(priorities):
        cd = dq.popleft()
        if cd < max(dq): # max 값이 아닌 경우 맨 뒤로
            dq.append(cd)    
        elif location == 0: # max 값인데 찾았을 경우 break
            break
        else: # max값인데 알고싶은 프로세스가 아닌 경우 
            answer += 1
        
        # location 업데이트
        location = len(dq) - 1 if location == 0 else location - 1
    return answer