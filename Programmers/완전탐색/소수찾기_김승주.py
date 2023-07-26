from itertools import permutations
import math


def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    nums_set = set()
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers, i):
            nums_set.add(int(''.join(num)))
    count = 0
    for num in nums_set:
        if isPrime(num):
            print(num)
            count += 1
    return count
