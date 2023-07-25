import heapq


def solution(jobs):
    answer = 0
    start = -1
    # 소요 시간 오름차순 정렬
    sorted_jobs = sorted(jobs, key=lambda x: x[1])

    while sorted_jobs:
        for i in range(len(sorted_jobs)):
            # 작업 시점이 start보다 작을 때
            if sorted_jobs[i][0] <= start:
                start += sorted_jobs[i][1]
                answer += start - sorted_jobs[i][0]
                sorted_jobs.pop(i)
                break
            # 반복문을 모두 돌았을 경우
            if i == len(sorted_jobs) - 1:
                start += 1
    return answer // len(jobs)

# import heapq
# def solution(jobs):
#     answer, now, i = 0, 0, 0
#     start = -1
#     heap = []

#     while i < len(jobs):
#         # 현재 시점에서 처리할 수 있는 작업들 저장
#         for j in jobs:
#             if start < j[0] <= now:
#                 heapq.heappush(heap, (j[1], j[0]))

#         if heap:
#             cur = heapq.heappop(heap)
#             start = now
#             now += cur[0]
#             answer += now - cur[1]
#             i += 1
#         else:
#             now += 1
#     return answer // i