import heapq


def solution(scoville, K):
    answer = 0
    q = []

    for e in scoville:
        heapq.heappush(q, e)

    while q:
        min_f = heapq.heappop(q)
        if q and min_f < K:
            min_s = heapq.heappop(q)
            v = min_f + (min_s * 2)
            heapq.heappush(q, v)
            answer += 1
        elif min_f >= K:
            heapq.heappush(q, min_f)
            break
        else:
            answer = -1

    return answer