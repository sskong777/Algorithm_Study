from collections import Counter
def solution(participant, completion):
    answer = ''
    c = Counter(participant)
    for x in completion:
        c[x] -= 1
    
    for k in c.keys():
        if c[k] != 0:
            return k

    return answer