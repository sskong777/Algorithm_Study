def solution(brown, yellow):
    answer = []

    for h in range(1, int(yellow ** (1 / 2)) + 1):  # 반만 진행
        # h: 세로 길이, w: 가로 길이
        if yellow % h == 0: # yellow의 약수인 경우
            w = yellow // h # 가로 길이

            if (w + 2) * (h + 2) - (w * h) == brown:    # 예상 brown의 크기에 yellow의 크기를 뺐을때 brown 값과 일치한지 확인
                answer = [w + 2, h + 2]
                break

    return answer
