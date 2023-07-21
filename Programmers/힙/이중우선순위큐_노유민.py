import heapq

def solution(operations):
    max_heap = []  # 최대힙을 저장하는 리스트
    min_heap = []  # 최소힙을 저장하는 리스트
    
    for op in operations:
        order, number = op.split(" ")
        number = int(number)
        
        if order == 'I':
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
        
        elif order == 'D':
            if not min_heap:  # 힙이 비어있을 경우 무시
                continue
            if number == -1:  # 최소값 제거
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-min_val)
                heapq.heapify(max_heap)
            elif number == 1:  # 최대값 제거
                max_val = -heapq.heappop(max_heap)
                min_heap.remove(max_val)
                heapq.heapify(min_heap)
    
    if min_heap:
        answer = [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        answer = [0, 0]
    
    return answer
