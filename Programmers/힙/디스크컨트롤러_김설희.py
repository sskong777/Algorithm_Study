import heapq
def solution(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1])) # x[0]이 같을 수도 있음 주의

    end_time = 0
    total_time = 0

    waiting_jobs = []

    while jobs or waiting_jobs:
        while jobs and jobs[0][0] <= end_time:
            request_time, duration = jobs.pop(0)
            heapq.heappush(waiting_jobs, (duration, request_time))

        if waiting_jobs:
            duration, request_time = heapq.heappop(waiting_jobs)
            end_time += duration
            total_time += end_time - request_time

        else:
            request_time, duration = jobs.pop(0)
            end_time = request_time + duration
            total_time += duration

    return total_time // n