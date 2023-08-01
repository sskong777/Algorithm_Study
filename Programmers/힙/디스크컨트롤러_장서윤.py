import heapq
from collections import deque


def solution(jobs):
    heap = []
    jobs = deque(sorted(jobs))

    sum = 0
    last = 0
    length = len(jobs)

    while jobs or heap:
        # jobs와 heap이 남아있는 동안 반복
        while jobs and jobs[0][0] <= last:
            # jobs가 남아있고, 현재 시간보다 작업 시작 시간이 빠른 것이 있다면 반복
            job = jobs.popleft()
            heapq.heappush(heap, [job[1], job[0]])  # 작업 시간을 기준으로 최소힙 만들기 위함

        if heap:    # heap에 들어온게 있으면
            time, start = heapq.heappop(heap)   # 작업을 뽑아냄
            last += time    # 현재 위치에서 작업 시간을 더해서 다음 위치를 잡아줌
            sum += last - start # 대기 시간 뺌

        else:  # 작업 시간이 빈 경우
            last = jobs[0][0]   # 현재 위치를 다음 작업의 시작 시간으로 업데이트 해줌

    return sum // length