# [15652] N과 M (4)

N, M = map(int, input().split())

result = []


def backtracking(num, i):
    if num == M:
        print(" ".join(map(str, result)))
        return
    for j in range(i, N+1):
        result.append(j)
        backtracking(num+1, j)
        result.pop()


backtracking(0, 1)
