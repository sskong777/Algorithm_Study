import math
from collections import deque

def solution(progresses, speeds):
    q = deque()
    for i in range(len(progresses)):
        q.append(math.ceil((100-progresses[i]) / speeds[i]))
    
    start = q.popleft()
    count = 1
    ans =[]
    while q:
        x = q.popleft()
        if(start >= x):
            count+=1
        else:
            start = x
            ans.append(count)
            count = 1
    ans.append(count)
    return ans