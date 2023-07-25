import heapq

def solution(operations):
    answer = [0, 0]
    
    queue = []
    
    
    for cLine in operations:
        
        c, d = cLine.split()
        
        if c == 'I':
            heapq.heappush(queue, int(d))
        elif c == 'D':
            if len(queue) == 0:
                continue
                
            if d == '1':
                heapq._heapify_max(queue)
                heapq.heappop(queue)
            elif d == '-1':
                heapq.heapify(queue)
                heapq.heappop(queue)
                

    if len(queue) != 0:
        heapq._heapify_max(queue)
        answer[0] = queue[0]
        heapq.heapify(queue)
        answer[1] = queue[0]
        
    
    return answer