def solution(answers):
    s1 = [1, 2, 3, 4, 5]  # 5
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10

    answer = []
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == s1[i % 5]:
            scores[0] += 1
        if answers[i] == s2[i % 8]:
            scores[1] += 1
        if answers[i] == s3[i % 10]:
            scores[2] += 1

    for idx, num in enumerate(scores):
        if num == max(scores):
            answer.append(idx + 1)

    return answer