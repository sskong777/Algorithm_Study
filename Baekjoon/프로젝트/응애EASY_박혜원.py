#[28088] 응애(EASY)
"""
동아리원의 수 N, 
처음에 인사를 하는 사람들의 수 M, 
인사를 진행하는 횟수 K, 
M명의 동아리원이 인사를 시작하는 위치
"""
from collections import deque

N, M, K = map(int, input().split())
hi = [0] * N+1

queue = deque(int(input()) for _ in range(M))

for _ in range(K):
# temp_queue : 다음 회차에서 인사를 시작할 동아리원들의 목록을 따로 관리
    temp_queue = deque()

    while queue:
        idx = queue.popleft()

        if 
