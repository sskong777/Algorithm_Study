def solution(arr):
    answer = []
    for num in arr:
        if not answer:
            answer.append(num)
        elif num != answer[-1]:
            answer.append(num)
        else:
            continue

    return answer