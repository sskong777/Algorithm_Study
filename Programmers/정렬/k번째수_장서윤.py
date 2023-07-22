def solution(array, commands):
    answer = []

    array = list(array)
    array.insert(0, 0)

    for i, j, k in commands:
        if i == j:
            arr = array[i]
            answer.append(arr)
            continue
        else:
            arr = array[i:j + 1]
            arr.sort()
            answer.append(arr[k - 1])

    return answer