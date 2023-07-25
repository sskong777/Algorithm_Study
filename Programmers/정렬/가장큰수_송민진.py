def solution(numbers):
    tmp = list(map(str, numbers))
    tmp.sort(reverse=True, key=lambda x: x*3)
    return str(int(''.join(tmp)))