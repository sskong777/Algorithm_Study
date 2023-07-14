import heapq


def solution(scoville, K):
    # heapify : 리스트를 힙으로 변환, 기존 리스트의 순서는 변경되지만 힙의 특성을 유지
    heapq.heapify(scoville)

    cnt = 0
    while scoville and scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        cnt += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return cnt