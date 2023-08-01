dict = {}
def solution(clothes):
    answer = 0
    for c in clothes:
        if c[1] in dict:
            dict[c[1]].append(c[0])
        else:
            dict[c[1]] = [c[0]]

    if len(dict) == 0:
        answer = len(dict[clothes[0][1]])
    else:
        tmp = 1
        for key in dict.keys():
            tmp *= (len(dict[key]) + 1)
        answer = tmp - 1
    return answer