def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start_index = commands[i][0]
        end_index = commands[i][1]
        k_index = commands[i][2]

        if start_index < 1 or end_index > len(array) or start_index > end_index:
            # 인덱스 범위를 초과하거나 시작 인덱스가 끝 인덱스보다 큰 경우 예외 처리한다.
            answer.append(-1)
        else:
            new_arr = array[start_index - 1:end_index]
            new_arr.sort()
            answer.append(new_arr[k_index - 1])

    return answer