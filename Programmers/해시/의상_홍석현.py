def solution(clothes):
    dict = {}
    for clothe, type in clothes:
        # 옷 종류별 이미 옷 종류가 있으면 해당 종류의 value에 +1, 없으면 0
        # 종류별 개수 세어주기 위한 dict
        dict[type] = dict.get(type, 0) + 1

    answer = 1
    for type in dict:
        answer *= (dict[type] + 1)

    return answer - 1

    # 각 type의 가지수를 통해 경우의 수 계산 후 -1