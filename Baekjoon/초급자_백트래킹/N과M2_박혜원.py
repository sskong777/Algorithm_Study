# [15650] N과M2
# N까지 자연수
# 조건을 만족하는 길이 M
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

"""
n, m = map(int, input().split())


result = []
check = [False] * (n+1)


def backtracking(num):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return

    for i in range(num, n+1):
        if check[i] == False:
            check[i] = True
            result.append(i)
            backtracking(i+1)  # 문제의 각 단계를 나타내는 인덱스를 증가시키며 탐색을 진행
            check[i] = False
            result.pop()


backtracking(1)
"""
# 방법 2
# i가 result 리스트에 포함되어 있지 않을 경우(즉 중복되지 않는다면) True를 반환하고, 리스트에 추가
# 포함되어 있을 경우 False를 반환
n, m = map(int, input().split())


result = []


def backtracking(num):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    for i in range(num, n+1):
        if i not in result:
            result.append(i)
            backtracking(i+1)
            result.pop()


backtracking(1)
