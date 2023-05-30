# [2346] 풍선 터뜨리기

from collections import deque

n = int(input())
paper = list(map(int, input().split()))  # 3 2 1 -3 -1
# balloon에 1부터 시작하는 인덱스와 함께 저장
# list 사용해야 인덱스와 값을 튜플로 묶은 리스트를 얻을 수 있다.
balloon = deque(list(enumerate(paper, start=1)))
result = []

while balloon:
    idx, step = balloon.popleft()  # 풍선 번호(idx)와 종이에 적힌 숫자(step) 추출
    result.append(idx)  # 결과에 추가

    if balloon:  # 아직 풍선이 남아있다면
        if step > 0:  # 종이에 적힌 숫자가 양수인 경우
            balloon.rotate(-(step-1))  # (step-1)만큼 오른쪽으로 회전
        else:  # 종이에 적힌 숫자가 음수인 경우
            balloon.rotate(-step)  # step만큼 왼쪽으로 회전

print(*result)  # 결과 출력
