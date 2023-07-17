import math

def solution(progresses, speeds):
    answer, idx = [], 0
    N = len(progresses)
    
    while idx < N:
        count = 0
        days = math.ceil((100 - progresses[idx]) / speeds[idx])
        
        for i in range(idx, N):
            progresses[i] += speeds[i] * days
            
        for i in range(idx, N):
            if progresses[i] >= 100: count += 1
            else: break
            
        answer.append(count)
        idx += count
            
    return answer