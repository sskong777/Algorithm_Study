import heapq


def solution(operations):
    answer = []

    heap = []

    for o in operations:
        c, n = o.split(" ")

        if c == "I":
            heapq.heappush(heap, int(n))

        elif c == "D" and heap:
            if n == "1":  # 최대값 삭제
                x = heapq.nlargest(n=1, iterable=heap)  # O(n log n)
                heap.remove(x[0])
                heapq.heapify(heap)  # O(n)

            elif n == "-1":  # 최소값 삭제
                heapq.heappop(heap)

    if not heap:
        answer = [0, 0]
    else:
        x = heapq.nlargest(n=1, iterable=heap)
        answer = [x[-1], heap[0]]

    return answer