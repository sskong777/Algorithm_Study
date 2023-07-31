from itertools import permutations
import math

def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    check = set()

    for i in range(1, len(numbers) + 1):
        li = list(permutations(numbers, i)) 
        number = list(int(''.join(j)) for j in li)

        for j in number:
            if is_prime(j) and j not in check:
                answer += 1
                check.add(j)
        
    return answer
