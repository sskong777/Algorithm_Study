'''
2가지 방법
1. itertools 사용
2. dfs 사용
'''


# 1. itertools 사용
from itertools import product

def solution(word):
    mo = ['A', 'E', 'I', 'O', 'U']
    mo_dict = []

    for length in range(1, 6):
        for comb in product(mo, repeat = length):
             mo_dict.append(''.join(comb))
 
    mo_dict.sort() # 정렬해야해서 배열로 바꿈
    return mo_dict.index(word) + 1

print(solution("AAAAE"))


