from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        count = 0
        
        while progresses and progresses[0] >= 100:
            # progresses 리스트가 비어있지 않은동안은 계속 반복 + 가장 앞에 있는 기능이 100 이상일 경우
            progresses.popleft()
            speeds.popleft()
            count += 1
            
        if count > 0:
            answer.append(count)

    return answer
