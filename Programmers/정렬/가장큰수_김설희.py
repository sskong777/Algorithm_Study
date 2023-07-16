def solution(numbers):
    str_numbers = list(map(str, numbers))
    max_length = max(len(s) for s in str_numbers)

    # 굳이 숫자로 비교할 필요 없었음
    sorted_numbers = sorted(str_numbers, key=lambda x: x * max_length, reverse=True)

    largest_number = ''.join(x for x in sorted_numbers)

    # [0,0,0,0] 이면 0000이니까 0으로 만들기
    if largest_number[0] == '0':
        return "0"

    return largest_number