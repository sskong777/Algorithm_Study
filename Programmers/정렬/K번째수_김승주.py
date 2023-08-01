def solution(array, commands):
    answer = []
    for command in commands:
        start, fin, find = command[0], command[1], command[2]
        answer.append(sorted(array[start-1:fin])[find-1])
    return answer