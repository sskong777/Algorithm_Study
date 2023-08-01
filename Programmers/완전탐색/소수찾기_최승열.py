from itertools import permutations
def isPrime(num):
    return all(num % i for i in range(2, int(num**0.5)+1))

def solution(numbers):
    answer, history = 0, {0, 1} # 0, 1은 무조건 소수가 아님
    numbers = list(map(str, numbers))
    
    for i in range(1, len(numbers)+1):
        for c in permutations(numbers, i):
            n = int("".join(c))
            
            if n in history: 
                continue
            history.add(n) # 한번 체크한 숫자는 체크하지 않기
            
            if isPrime(n): 
                answer += 1
    return answer