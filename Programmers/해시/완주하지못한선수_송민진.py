from collections import deque

def solution(participant, completion):
    answer = ''
    participant.sort()
    p_q = deque(participant)
    completion.sort()

    for c in completion:
        checking = p_q.popleft()
        if c != checking:
            answer = checking
            break
    if answer == "":
        answer = p_q.popleft()
    return answer