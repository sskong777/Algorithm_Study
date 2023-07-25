import heapq

def solution(operations):
    min_heap = []

    for o in operations:
        command, target = o.split()
        if command == 'I':
            heapq.heappush(min_heap, int(target))
        else:
            if not min_heap:
                continue
            if target == '-1':
                heapq.heappop(min_heap)
            else:
                min_heap.pop()

    if len(min_heap) > 1:
        # return [min_heap.pop(), heapq.heappop(min_heap)]      -> 틀림
        return [max(min_heap), heapq.heappop(min_heap)]
    elif len(min_heap) == 1:
        return [min_heap[0]] * 2
    return [0, 0]