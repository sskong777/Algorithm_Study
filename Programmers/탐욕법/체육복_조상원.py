from collections import Counter
def solution(n, lost, reserve):
    only_res = set(reserve) - set(lost)
    only_lost = set(lost) - set(reserve)

    arr = [1] * (n+1)
    
    for r in only_res:
        if r-1 in only_lost:
            only_lost.remove(r-1)
        elif r+1 in only_lost:
            only_lost.remove(r+1)
    
    return n - len(only_lost)
    
