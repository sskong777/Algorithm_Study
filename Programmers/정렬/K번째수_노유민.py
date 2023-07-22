def solution(array, commands):
    answer = []
    for order in commands:
        start = order[0]-1
        end = order[1]
        want = order[2]-1
        answer.append(sorted(array[start:end])[want])
    return answer