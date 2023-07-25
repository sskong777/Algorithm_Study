import heapq
def solution(c):
    answer = 0
    
    if len(c) == 1:
        return c[0]
    
    c = sorted(c, reverse=True)
    t = 0
    # print(c)
    for i, v in enumerate(c):
        # print('i', i, 'v', v)
        if (i+1) <= v:
            t = i+1
        else:
            return t
                
    return t    
#     print(h)
#     # 0 1 3 5 6
#     return h