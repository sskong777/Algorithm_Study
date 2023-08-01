def solution(clothes):
    answer = 1
    dic = dict()

    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1

    for key in dic.keys():
        answer *= dic[key] +1

    return answer -1