def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    oi = twi = thi = 0
    oc = twc = thc = 0
    
    for n in answers:
        if n == one[oi]:
            oc += 1
        if n == two[twi]:
            twc += 1
        if n == three[thi]:
            thc += 1
        oi += 1
        twi += 1
        thi += 1
        if oi == len(one):
            oi = 0
        if twi == len(two):
            twi = 0
        if thi == len(three):
            thi = 0
    
    top = max(oc, twc, thc)
    for i, v in enumerate([oc, twc, thc]):
        if v == top:
            answer.append(i+1)
    return answer