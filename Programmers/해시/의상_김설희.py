def solution(clothes):
    dressroom = {}
    for i in clothes:
        if i[1] not in dressroom:
            dressroom[i[1]] = 1
        else:
            dressroom[i[1]] += 1

    result = 1
    for value in dressroom.values():
        result *= (value + 1)

    return result - 1