# [1966] 프린터 큐
import sys
from collections import deque

test_case = int(input())

for _ in range(test_case):
    count = 0
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, input().split())))

    while len(queue) > 0:
        if queue[0] == max(queue):
            queue.popleft()
            if m == 0:
                count += 1
                break
            else:
                count += 1
                m -= 1
        else:
            a = queue.popleft()
            queue.append(a)
            if m == 0:
                m += len(queue) - 1  # 목표 수가 최대값이 아니면 맨 뒤로 넣어줌
            else:
                m -= 1
    print(count)
