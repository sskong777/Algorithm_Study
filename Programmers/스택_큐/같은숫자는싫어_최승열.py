def solution(arr):
    return [a for i, a in enumerate(arr) if i == 0 or (arr[i] != arr[i-1])]