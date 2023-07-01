participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    answer = dict()

    for p in participant:
        if p in answer.keys():
            answer[p] += 1
        else:
            answer[p] = 1

    for c in completion:
        answer[c] -= 1
        if answer[c] == 0:
            answer.pop(c)

    return answer.popitem()[0]
