from collections import deque
# 단순히 개수로 따지면 안됨.( 순서도 중요 )
def solution(s):
    
    q = deque([])
    for i in range(len(s)):
        if s[i] == '(':
            q.append(s[i])
        else:
            if len(q) == 0:
                return False
            else:
                q.pop()
    if len(q)!=0:
        return False
        
    return True