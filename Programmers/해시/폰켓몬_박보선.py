from collections import Counter
def solution(nums):
    answer = 0
    pokemon = Counter(nums)
    
    m = len(nums) // 2

    c = len(list(pokemon.keys()))
    
    if m > c:
        answer = c
    else:
        answer = m
    
    return answer