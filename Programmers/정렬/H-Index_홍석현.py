def solution(array):
    answer = 0
    array.sort()

    for i in range(len(array)):
        if array[i] >= len(array) - i:
            answer = len(array) - i
            break

    return answer