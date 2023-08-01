import heapq
def solution(operations):
    heap = []
    for oper in operations:
        command, num = oper.split(' ')
        if command == 'I':
            heapq.heappush(heap, int(num))
        elif heap and command =='D':
            # 최대힙을 구해서 삭제해야함
            # nlargest를 통해 가장 큰 수를 찾아서 heap의 인덱스로 위치를 이용해 삭제
            if num == '1':
                heap.pop(heap.index(
                    heapq.nlargest(1, heap)[0])
                     )
            elif num == '-1':
                heapq.heappop(heap)
                # 최소 힙 삭제
    if not heap:
        return [0,0]
    else:
        # 최대힙과 최소힙 리턴
        return [heapq.nlargest(1,heap)[0], heap[0]]
