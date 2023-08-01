import itertools


def solution(numbers):
    answer = 0
    arr = []
    for l in range(1, len(numbers) + 1):
        tmp = list(itertools.permutations(list(numbers), l))
        arr += list(map(lambda x: int(''.join(x)), tmp))
    arr = set(arr)

    # 에라토스테네스의 체
    n = max(arr)
    prime = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if prime[i]:
            for j in range(2 * i, n + 1, i):
                prime[j] = False

    for num in arr:
        if prime[num]:
            answer += 1
    return answer