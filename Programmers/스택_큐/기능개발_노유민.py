import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    # deque 선언
    finish = deque()
    for p, s in zip(progresses, speeds):
        # 남은 퍼센트를 speeds로 나눠서 올림
        finish.append(math.ceil((100-p)/s))

    firstFinal = finish.popleft()
    count = 1
    for i in finish:
        # 앞의 일정이 더 길면
        if firstFinal >= i:
            count += 1
        else:
            # 앞의 일정이 더 짧으면 지금까지 count 넣기
            answer.append(count)
            count = 1
            firstFinal = i
    # 마지막 count 넣기
    answer.append(count)

    return answer
