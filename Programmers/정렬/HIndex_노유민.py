def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    count = 0
    for i in citations:
        count+=1
        if i >= count and count >=answer:
            answer=count
            
    return answer