def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def dfs(numbers, current, check, result):
    if current:
        n = int(''.join(current))
        if is_prime(n):
            result.add(n)

    for i in range(len(numbers)):
        if check[i] == 0:
            check[i] = 1
            current.append(numbers[i])
            dfs(numbers, current, check, result)
            current.pop()
            check[i] = 0


def solution(numbers):
    check = [0] * len(numbers)
    result = set()
    dfs(numbers, [], check, result)

    return len(result)