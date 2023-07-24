'''
시간 초과 코드
from itertools import permutations

def solution(numbers):
    arr = list(permutations(numbers, len(numbers)))
    new_arr = []
    for in_arr in arr:
        int_new = int(''.join(str(num) for num in in_arr))
        new_arr.append(int_new)

    return max(new_arr)
'''
#으악 모르겠다
from functools import cmp_to_key

def compare(a, b):
    num1 = int(a + b)
    num2 = int(b + a)

    if num1 > num2:
        return -1  # a가 b보다 큰 경우
    elif num1 < num2:
        return 1  # b가 a보다 큰 경우
    else:
        return 0  # 두 수가 같은 경우

def solution(numbers):
    # 리스트를 문자열로 변환하여 정렬 기준을 비교 함수로 지정
    numbers = sorted(map(str, numbers), key=cmp_to_key(compare))
    # 0으로만 이루어진 배열인 경우 '0'을 반환
    if numbers[0] == '0':
        return '0'
    # 정렬된 숫자 배열을 이어붙여 가장 큰 수를 생성하여 반환
    return ''.join(numbers)

# 테스트
numbers = [6, 10, 2]
print(solution(numbers))  # Output: "6210"


#이건 무슨 풀이요?
def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
