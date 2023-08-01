'''
[1, 1, 1, 1, 1]
3

[4, 1, 2, 1]
4
'''

def dfs(v, total, numbers, target):

    cnt = 0

    if v == len(numbers):
        if total == target:
            return 1
        return 0

    cnt += dfs(v + 1, total + numbers[v], numbers, target)
    cnt += dfs(v + 1, total - numbers[v], numbers, target)

    return cnt

def solution(numbers, target):

    return dfs(0, 0, numbers, target)
