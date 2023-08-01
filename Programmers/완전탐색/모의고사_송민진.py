def solution(answers):
    result = []
    tmp = [0, 0, 0]
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if supo1[i % 5] == answers[i]:
            tmp[0] += 1
        if supo2[i % 8] == answers[i]:
            tmp[1] += 1
        if supo3[i % 10] == answers[i]:
            tmp[2] += 1

    res = max(tmp)
    for j in range(len(tmp)):
        if tmp[j] == res:
            result.append(j + 1)
    return result