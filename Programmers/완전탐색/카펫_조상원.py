def solution(brown, yellow):
    answer = []
    if yellow == 1 and brown == 8:
        return [3, 3]
    brown -= 4
    for w in range(1, yellow // 2 + 1):
        if yellow % w != 0:
            continue
        h = int(yellow / w)
        need = h * 2 + w * 2
        if need == brown:
            return [h+2, w+2]
        # print(w, h)
        # print(i)
    return answer