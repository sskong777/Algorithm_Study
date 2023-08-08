def solution(routes):
    answer = 1

    # 진입지점을 기준으로 오름차순 정렬
    routes.sort(key=lambda x: x[0])

    # 진입/진출 초기값 세팅
    start = routes[0][0]
    end = routes[0][1]

    for i in range(1, len(routes)):
        if start <= routes[i][0] <= end:  # 다음 차량이 진입/진출 지점 사이에 있는 경우
            start = max(routes[i][0], start)  # 카메라 설치 최소 지점 갱신
            end = min(routes[i][1], end)  # 진출 지점 범위를 좁혀서 설치 지점의 범위를 줄임
        else:  # 사이에 없는 경우
            answer += 1  # 카메라 추가 설치
            end = max(routes[i][1], end)  # 진출 지점을 다음 범위로 늘림

    return answer