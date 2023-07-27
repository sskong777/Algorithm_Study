def solution(sizes):
    resizes = []

    w, h = 0, 0

    # 가로, 세로 중에서 큰 값은 resizes 의 0번 인덱스에 저장
    for size in sizes:
        if size[0] > size[1]:
            resizes.append([size[0], size[1]])
        else:
            resizes.append([size[1], size[0]])

    # 가로 값 중 가장 큰 값을 w에 저장하고, 세로 값 중 가장 큰 값을 h에 저장
    for re in resizes:
        if re[0] > w:
            w = re[0]

        if re[1] > h:
            h = re[1]

    return w * h
