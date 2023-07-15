from collections import deque
def solution(priorities, location):
    answer = location
    priorities = deque(priorities)
    
    
    count = 0
    while answer!=-1:
        if priorities[0] == max(priorities):
            priorities.popleft()
            answer-=1
            count+=1
        else:
            priorities.rotate(-1)
            if answer ==0:
                answer=len(priorities)-1
            else:
                answer-=1
            
    
    return count