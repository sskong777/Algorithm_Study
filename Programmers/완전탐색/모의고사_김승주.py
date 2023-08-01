def solution(answers):
    answer = [0] * 3

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if supo1[i % 5] == answers[i]:
            answer[0] += 1
        if supo2[i % 8] == answers[i]:
            answer[1] += 1
        if supo3[i % 10] == answers[i]:
            answer[2] += 1
    m = max(answer)
    return [index+1 for index, val in enumerate(answer) if val == m]
