from collections import deque
def solution(people, limit):
    answer = 0
    _len = len(people)
    people.sort(reverse=True)
    people = deque(people)
    
    while _len>1:
        if people[0]+people[-1]<=limit:
            people.popleft()
            people.pop()
            _len-=2
        else:
            people.popleft()
            _len-=1
        answer+=1
        
    if people:
        answer+=1
    return answer
