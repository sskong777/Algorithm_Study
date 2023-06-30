def solution(participant, completion):
    # completion의 길이는 participant의 길이보다 1 작습니다.
    hashDict = {}
    sumHash = 0
    for p in participant:
        hashDict[hash(p)] = p
        sumHash += hash(p)

    for c in completion:
        sumHash -= hash(c)

    return hashDict[sumHash]