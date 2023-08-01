from itertools import *


def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    result = []

    for i in range(1, len(words) + 1):  # 숫자 자리수
        for j in list(product(words, repeat=i)):    # 중복 순열로 계산
            result.append(''.join(j))   # 조합해서 리스트에 저장

    result.sort()   # 정렬

    return result.index(word) + 1   # 인덱스 값으로 순서 찾음
