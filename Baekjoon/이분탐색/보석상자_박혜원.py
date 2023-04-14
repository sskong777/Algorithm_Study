# [2792] 보석상자
# 나눠줄 보석의 수 (mid = 질투심), 질투심 최솟값 출력!
# 인원수 n 색상 종류 수 k


n, k = map(int, input().split())
colors = [int(input()) for _ in range(k)]

start, end = 1, max(colors)

while start <= end:
    mid = (start + end) // 2
    person_per_jewel = 0

    for color in colors:
        if color % mid == 0:
            person_per_jewel += color // mid
        else:   # 나머지가 존재한다면? 해당 보석을 모두 나눠주어야 하니까 1명 더 추가
            person_per_jewel += (color // mid) + 1
    if person_per_jewel <= n:    # mid가 보석의 최댓값인 7 이상이면 나눠줄 학생수의 최대가 5로 일정해진다.
        answer = mid             # 답을 출력하고,  mid(질투심)의 최소를 찾기위해 end를 1씩 낮춰본다
        end = mid - 1
    # 쥬얼리를 너무 조금씩 나눠서 받는 학생의 수가 많으므로, 나눠주는 보석의 수(mid) 높이기!
    else:
        start = mid + 1
print(answer)
