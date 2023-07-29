import math
def solution(brown, yellow):
    answer = []
    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow %i==0:
            width = (yellow//i+2)*2
            height = i*2
            if brown ==(width+height):
                answer.append(yellow//i+2)
                answer.append(i+2)
    
    return answer