def solution(brown, yellow):
    answer = []
    
    if yellow == 1:
        return [3, 3]
    
    for i in range(1, yellow // 2 + 1):
        if yellow % i != 0:
            continue
        row = i + 2
        col = yellow // i + 2
        if row * col - yellow == brown:
            answer.append(max(row, col))
            answer.append(min(row, col))
            break
    
    
    return answer