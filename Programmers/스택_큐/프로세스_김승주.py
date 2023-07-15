from collections import deque

def solution(priorities, location):
    q = deque([])
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    
    count = 0
    
    while q:
        i, p = q.popleft()
        
        if (p < max([x[1] for x in q])) :
            q.append((i, p))
        else:
            count+=1
            if(i == location):
                return count
        if(len(q) == 1 ): # 여기서 테스트 케이스 2,5,8 예외 발생 했었음
            return count+1
    return count