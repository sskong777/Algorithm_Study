# [9375] 패션왕 신해빈
T = int(input())

for _ in range(T):
    N = int(input())  # 의상의 수
    clothes = {}
    for i in range(N):
        name, category = input().split()
        # 이미 등록된 의상의 종류라면, 해당 의상의 개수를 1 증가
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    # 최종적으로 해빈이가 의상을 입을 수 있는 방법의 수
    cnt = 1
