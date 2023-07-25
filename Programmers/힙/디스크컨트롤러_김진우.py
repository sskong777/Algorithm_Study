'''import heapq


def solution(jobs):
    answer = 0
    start_time = 0  # 현재 시간
    end_time = 0  # 작업이 끝난 시간
    jobs.sort()  # 요청 시간 기준으로 정렬된 리스트

    # 작업이 완료된 시간까지 모든 작업이 처리될 때까지 반복
    while jobs:
        # 힙을 사용하여 소요 시간이 가장 짧은 작업 선택
        heap = []
        for job in jobs:
            if job[0] <= end_time:
                heapq.heappush(heap, (job[1], job[0]))
        if heap:
            job_time, job_request = heapq.heappop(heap)
            start_time = end_time
            end_time += job_time
            answer += (end_time - job_request)
            jobs.remove([job_request, job_time])
        else:
            end_time += 1

    # 평균 작업 시간 계산
    answer //= len(jobs)
    return answer


# 예시 입력과 호출
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
'''

'''import heapq

def solution(jobs):
    answer = 0
    start_time = 0  # 현재 시간
    total_time = 0  # 작업 시간의 총합
    heap = []  # 힙을 사용한 대기열

    jobs.sort(key=lambda x: x[0])  # 요청 시간을 기준으로 작업들을 정렬

    while jobs or heap:
        # 현재 시간 이하인 작업들을 대기열에 추가
        while jobs and jobs[0][0] <= start_time:
            request_time, processing_time = jobs.pop(0)
            heapq.heappush(heap, (processing_time, request_time))

        if heap:
            processing_time, request_time = heapq.heappop(heap)
            start_time += processing_time
            total_time += start_time - request_time
        else:
            start_time = jobs[0][0]

    answer = total_time // len(jobs)
    return answer

# 테스트
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))  # 결과: 9
'''

import heapq


def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort()  # 요청 시간순으로 정렬

    current_time, total_time = 0, 0
    min_heap = []  # 우선순위 큐(최소힙)

    while jobs or min_heap:
        # 대기 작업 중인 작업들 중에서 현재 시간 이전에 요청된 작업들을 힙에 추가
        while jobs and jobs[0][0] <= current_time:
            requested_time, processing_time = jobs.pop(0)
            heapq.heappush(min_heap, (processing_time, requested_time))

        if min_heap:
            # 가장 짧은 작업 시간이 소요되는 작업 처리
            processing_time, requested_time = heapq.heappop(min_heap)
            current_time += processing_time
            total_time += (current_time - requested_time)
        else:
            # 대기 작업이 없을 경우, 다음 작업 요청 시간으로 시간 이동
            current_time = jobs[0][0]

    answer = total_time // n
    return answer
