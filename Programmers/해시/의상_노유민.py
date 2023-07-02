def solution(clothes):
    answer = 1
    wear = {}

    for i in clothes:
        if i[1] in wear:
            wear[i[1]].append(i[0])
        else:
            wear[i[1]] = [i[0]]

    for i in wear:
        answer *= (len(wear[i])+1)
    answer -= 1
    return answer
