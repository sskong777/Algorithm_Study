# 섞은 음식의 스코빌 지수 =
# 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

import heapq

def solution(scoville, K):
    # 스코빌 지수 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)
    mix_count = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        # 가장 덜 매운 음식과 그 다음으로 덜 매운 음식을 섞어서 새로운 음식 생성
        new_food = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_food)
        mix_count += 1

    return mix_count

# 테스트 예시
print(solution([1, 2, 3, 9, 10, 12], 7))  # Output: 2
