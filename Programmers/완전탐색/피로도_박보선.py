from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    order = [i for i in range(len(dungeons))]
    
    order_list = list(permutations(order, len(dungeons)))

    for ol in order_list:
        temp = 0
        f = k
        for o in ol:
            a, b = dungeons[o]
            if f >= a:
                f -= b
                temp += 1
        
        answer = max(answer, temp)
        
    
    return answer