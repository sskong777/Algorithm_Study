# [20301] 반전 요세푸스
"""
[1,2,3,4,5,6,7] 
K = 3번째 마다 지우기
1,2을 7뒤로 append해주고, 맨 앞에 있는 3를 popleft해주고 print하는 방식

지운 횟수가 M번이 되면 방향을 바꿔주기
"""
from collections import deque

N, K, M = map(int, input().split())  # 7 3 4
"""
N명이 원을 이루며 앉아있다
M명마다 지우기
K명이 되면 사람을 제거하는 순서 반대로 돌리기
"""

people = deque(range(1, N+1))  # 1부터 N까지의 숫자를 deque에 넣음
direction = 1  # 처음에는 오른쪽 방향으로 진행
count = 0  # 제거한 사람의 수

while people:
    if direction == 1:  # 오른쪽 방향으로 진행
        for _ in range(K-1):
            people.append(people.popleft())  # K번째 사람을 찾음
        print(people.popleft())  # K번째 사람을 제거하고 번호를 출력
    else:  # 왼쪽 방향으로 진행
        for _ in range(K-1):
            people.appendleft(people.pop())  # K번째 사람을 찾음
        print(people.pop())  # K번째 사람을 제거하고 번호를 출력

    count += 1
    if count % M == 0:  # M명의 사람을 제거했으면
        direction *= -1  # 방향을 바꿈
