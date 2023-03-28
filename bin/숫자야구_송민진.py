import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

n = int(input())
trials = []
numbers = deque(map(list, permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)))

for _ in range(n):
    num, strike, ball = input().strip().split()
    trials.append([list(map(int, list(num))), int(strike), int(ball)])

for trial_num, strike_cnt, ball_cnt in trials:
    tmp = deque([])
    while numbers:
        can_continue = True
        checking = list(numbers.popleft())
        # 정답일 가능성 체크
        # 1. 이미 나온 오답과 같은지 체크
        if checking == trial_num:
            continue
        else:
            s_cnt, b_cnt = 0, 0
            # 2-1. strike 체크
            if trial_num[0] == checking[0]: s_cnt += 1
            if trial_num[1] == checking[1]: s_cnt += 1
            if trial_num[2] == checking[2]: s_cnt += 1
            # 2-1. ball 체크
            if trial_num[0] == checking[1]: b_cnt += 1
            if trial_num[0] == checking[2]: b_cnt += 1
            if trial_num[1] == checking[0]: b_cnt += 1
            if trial_num[1] == checking[2]: b_cnt += 1
            if trial_num[2] == checking[0]: b_cnt += 1
            if trial_num[2] == checking[1]: b_cnt += 1
            if s_cnt == strike_cnt and b_cnt == ball_cnt:
               tmp.append(checking)
    numbers = tmp

print(len(numbers))