'''def solution(clothes):
    answer = 0
    return answer

clothes = [["yellow_hat", "headgear"],
           ["blue_sunglasses", "eyewear"],
           ["green_turban", "headgear"]]'''


def solution(clothes):
    closet = {}  # 의상의 종류별로 개수를 저장할 딕셔너리

    # 의상의 종류별로 개수를 세어서 딕셔너리에 저장
    for item, category in clothes:
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1

    answer = 1  # 의상을 선택하는 경우의 수를 저장할 변수

    # 의상의 종류별로 선택할 수 있는 경우의 수 계산
    for count in closet.values():
        answer *= (count + 1)  # 해당 종류의 의상을 입지 않는 경우까지 고려하여 곱해줌

    answer -= 1  # 아무 의상도 입지 않은 경우를 제외

    return answer


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

solution(clothes)