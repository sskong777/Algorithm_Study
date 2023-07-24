def solution(citations):
    answer = 0
    length = len(citations)
    citations.sort()
    
    for i in range(length):
        f = i
        e = length - f
        
        if citations[i] >= e:
            answer = e
            break
        
    return answer