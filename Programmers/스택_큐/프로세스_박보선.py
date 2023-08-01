from collections import deque
def solution(priorities, location):
    answer = 0
    stack = []
    
    for i in range(len(priorities)):
        stack.append([i, priorities[i]])
    
    stack = deque(stack)
    priorities.sort()

    while stack:
        i, p = stack.popleft()
        
        if p < priorities[-1]:
            stack.append([i, p])
        elif p == priorities[-1]:
            answer += 1
            priorities.pop()
            if i == location:
                break
    
    
    
    return answer