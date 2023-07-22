def solution(numbers):
    answer = ''

    num_list = []

    # 숫자를 6자리로 만들어서 비교함
    for num in numbers:
        n = ''
        while len(n) <= 6:
            n += str(num)
        num_list.append([n, str(num)])

    num_list.sort(reverse=True)

    # 문자를 합쳐서 반환
    for n in num_list:
        answer += n[1]

    return str(int(answer))