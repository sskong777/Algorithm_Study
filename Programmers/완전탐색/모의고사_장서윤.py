def solution(answers):
    answer = []

    students = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    ls = []
    length = len(answers)
    for n, student in enumerate(students):
        tmp = 0
        while len(student) < length:    # 정답의 길이만큼 수포자의 답 패턴을 늘려줌
            student += student

        for s, a in zip(student, answers):  # 정답과 수포자가 찍은 답과 비교함
            if s == a:
                tmp += 1
        ls.append([n + 1, tmp]) # 수포자 번호와 맞은 개수를 리스트에 저장

    ls.sort(key=lambda x: (x[1]), reverse=True) # 맞은 개수를 기준으로 정렬함

    max_ = ls[0][1] # 가장 많이 맞힌 학생의 점수를 저장

    if max_ == 0:   # 맞힌 사람이 아무도 없는 경우 빈 리스트 반환
        return []

    for n, tmp in ls:
        if tmp - max_ >= 0:     # 수포자의 점수에 많이 가장 많이 맞힌 학생의 점수를 뺐을때 0 이상이 나오면
            answer.append(n)    # answer 리스트에 학생 번호 저장

    return answer