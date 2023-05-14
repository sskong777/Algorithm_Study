import sys
from collections import deque

test_cases = int(sys.stdin.readline())

results = []
for _ in range(test_cases):
    num_docs, target_idx = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))

    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0

    while queue:
        doc_idx, priority = queue.popleft() 
        if any(priority < p for _, p in queue):
            queue.append((doc_idx, priority))
        else:
            count += 1
            if doc_idx == target_idx:
                results.append(count)
                break

for result in results:
    print(result)
