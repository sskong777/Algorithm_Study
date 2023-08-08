def solution(n, lost, reserve):
    answer = 0
    # 각각 중복된 요소 제거 (set 이용)
    # reserve set
    reserve_set = set(reserve) - set(lost)
    # lost set
    lost_set = set(lost) - set(reserve)

    # 빌려줄 수 있는 학생들의 앞 뒤 번호가 lost set에 있으면 lost set에서 제거
    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)

        elif i + 1 in lost_set:
            lost_set.remove(i + 1)

            # lost set
    answer = n - len(lost_set)

    return answer