def solution(participant, completion):
    li = {}
    answer = ""
    for i in participant:
        if i in li:
            li[i] += 1
        else:
            li[i] = 1

    for i in completion:
        if (i in li):
            li[i] -= 1
            if li[i] == 0:
                del(li[i])

    answer += next(iter(li))

    return answer
