def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_ans = 0
    b_ans = 0
    c_ans = 0
    
    
    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            a_ans += 1
        if b[i%8] == answers[i]:
            b_ans += 1
        if c[i%10] == answers[i]:
            c_ans += 1            
    
    k = max([a_ans, b_ans, c_ans])
    
    if k == a_ans:
        answer.append(1)
    if k == b_ans:
        answer.append(2)
    if k == c_ans:
        answer.append(3)
    
    
    
    return answer