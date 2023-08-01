def solution(clothes):
    answer = 1

    clothe_dict = dict()
    
    for c, w in clothes:
        clothe_dict[w] = clothe_dict.get(w, 0) + 1
    
    for val in clothe_dict.values():
        answer *= (val + 1)
    
    # 아무것도 안 입었을때의 경우 -1
    return answer - 1