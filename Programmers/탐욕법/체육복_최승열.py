def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    
    common = lost.intersection(reserve)
    lost -= common
    reserve -= common
    
    for r in reserve:
        if r-1 in lost: 
            lost.remove(r-1)
        elif r+1 in lost: 
            lost.remove(r+1)
    
    return n - len(lost)