from heapq import heappop, heappush

def solution(jobs):
    answer = 0
    now = 0
    n = len(jobs)
    min_heap = []

    jobs.sort()

    while jobs or min_heap:
        if not min_heap and jobs[0][0] > now:
            now = jobs[0][0]

        while jobs and jobs[0][0] <= now:
            request_time, cost = jobs.pop(0)
            heappush(min_heap, (cost, request_time))

        if min_heap:
            cost, request_time = heappop(min_heap)
            answer += (now - request_time) + cost
            now += cost
        else:
            now += 1

    return answer // n