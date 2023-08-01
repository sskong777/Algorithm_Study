def solution(sizes):
    answer = 0

    for sub_list in sizes:
        sub_list.sort()

    W = max(sizes, key = lambda x: x[0] )
    H = max(sizes, key = lambda x: x[1])
    answer = W[0] * H[1]
    
    return answer
