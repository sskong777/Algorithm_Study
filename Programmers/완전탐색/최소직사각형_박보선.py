def solution(sizes):
    answer = 1000001
    n = len(sizes)
    width = []
    height = []
    
    for i in range(n):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
    
    answer = max(width) * max(height)
    
    
    
    return answer