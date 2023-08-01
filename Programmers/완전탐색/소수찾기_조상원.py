from itertools import permutations
def solution(numbers):
    answer = 0
    visited = set()
    
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    cnt = 0
    for i in range(1, len(numbers) + 1):
        perms = list(permutations(numbers, i))
        for n in perms:
            check = int(''.join(n))
            if is_prime(check) and check not in visited:
                visited.add(check)
                print(check)
                cnt+=1
                
    print(cnt)
    return cnt