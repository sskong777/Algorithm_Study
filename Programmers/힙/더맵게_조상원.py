import heapq
def solution(scoville, K):
    cnt = 0
    
    heapq.heapify(scoville)
    
    # 모든 값이 음수이면 불가능
    if all(i < 0 for i in scoville):
        return -1
    # 하나밖에 없으면 K랑 비교
    if len(scoville) == 1:
        return 0 if scoville[0] < K else -1
    
    while scoville:
        # 최솟값
        low = heapq.heappop(scoville)
        if low < K:
            # 두번째 값을 가져올 수 있으면
            if scoville:
                second = heapq.heappop(scoville)
                heapq.heappush(scoville, low + second * 2)
                cnt+=1
            # 두번째 값이 없고 최솟값이 K이하
            else:
                cnt = -1
                break
        else:
            break
    return cnt