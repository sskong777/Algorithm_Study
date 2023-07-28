from itertools import combinations, permutations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    primes = set()
    # nums = list(map(int,list(numbers)))
    nums = list(numbers)
    for i in range(1, len(nums) + 1):
        num_list = permutations(nums, i)
        for j in num_list:
            new_num = int(''.join(j))
            if is_prime(new_num):
                primes.add(new_num)

    return len(primes)


