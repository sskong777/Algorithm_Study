# [2792] 보석상자
# 나눠줄 보석의 수 (mid = 질투심), 질투심 최솟값 출력!
# 인원수 n 색상 종류 수 m


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
    if person_per_jewel <= n:    # 보석이 남았다면 = 나눠줘야 할 사람이 더 필요한 경우
        answer = mid
        end = mid - 1
    else:                 # 보석을 n명의 사람에게 전부 나눠줄 수 있다면
        start = mid + 1
print(answer)
