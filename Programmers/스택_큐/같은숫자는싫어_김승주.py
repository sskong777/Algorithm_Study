def solution(arr):
    answer = []
    prev = arr[0]
    answer.append(prev)
    for i in range(len(arr)):
        if prev != arr[i]:
            answer.append(arr[i])
            prev = arr[i]
    
    return answer