'''
큐를 2개 만들고 queue와 minqueue는 절반씩 필요가 없음
'''

import heapq
import time
def solution(operations):
    queue = []
    minusqueue = []
    qsize = 0

    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(queue, int(operation[2:]))
            heapq.heappush(minusqueue, -int(operation[2:]))
            qsize += 1
            continue

        if operation == "D -1":
            if queue:
                heapq.heappop(queue)
                qsize -= 1

        elif operation == "D 1":
            if minusqueue:
                heapq.heappop(minusqueue)
                qsize -= 1

        if qsize == 0:
            queue.clear()
            minusqueue.clear()

    if qsize == 0:
        return [0, 0]
    else:
        return [-minusqueue[0], queue[0]]


# L = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] * 100000
# t1 = time.time()
# print(solution(L))
# print(time.time()-t1)
