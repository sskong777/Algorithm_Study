def solution(array, commands):
    answer = []
    for com in commands:
        start, end, target = com
        answer.append(sorted(array[start-1:end])[target-1])
    return answer