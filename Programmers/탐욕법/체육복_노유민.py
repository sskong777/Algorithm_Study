def solution(n, lost, reserve):
    setLost = set(lost)-set(reserve)
    setReserve = set(reserve)- set(lost)
    
    for i in setReserve:
        if i-1 in setLost:
            setLost.remove(i-1)
        elif i+1 in setLost:
            setLost.remove(i+1)
    answer = n-len(setLost)
#     reserve.sort()
#     lost.sort()
    
#     for i in reserve:
#         if i in lost:
#             lost.remove(i)
#             reserve.remove(i)

#     length = len(lost)
#     answer=n-length
    
#     for i in reserve:
#         if i-1 in lost:
#             answer+=1
#             lost.remove(i-1)

#         elif i+1 in lost:
#             answer+=1
#             lost.remove(i+1)

    return answer