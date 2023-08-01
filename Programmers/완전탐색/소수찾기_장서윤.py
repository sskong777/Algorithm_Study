from itertools import *


def sieve_of_eratosthenes(num): # 소수구하기 에라토스테네스의 체

    arr = [True for i in range(num + 1)]

    for i in range(2, int(num ** (1 / 2)) + 1):
        if arr[i]:
            j = 2
            while i * j <= num:
                arr[i * j] = False
                j += 1

    return arr


def solution(numbers):
    answer = 0
    result = []

    # 문자열 분리
    num = list(numbers)

    # 글자수에 따라 순열 구하기
    for i in range(1, len(num)+1):
        for j in list(permutations(num, i)):
            result.append(int(''.join(j)))

    # 중복 값 제거 후 정렬
    result = list(set(result))
    result.sort()

    # 가장 큰 수로 에라토스테네스의 체 돌림
    n = sieve_of_eratosthenes(result[-1])

    # 순열을 하나씩 돌면서 소수 찾음
    for i in result:
        if n[i] and i > 1:
            answer+=1

    return answer