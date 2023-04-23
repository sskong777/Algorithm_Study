# [15649] N과 M(1)
N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 출력
# # 방법 1. itertools 이용
# import itertools
# n = [i for i in range(1, N+1)]
# lists = itertools.permutations(n, M)
# answer = []
# for arr in lists:
#     answer.append(' '.join(map(str, arr)))

# answer.sort()
# for ans in answer:
#     print(ans)

# 방법 2. 백트래킹 구현 - 각 조합 하나씩 구해서 바로바로 출력
arr = []
isused = [0]*(N+1)
def backtracking():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1):
        if isused[i] == 1:
            continue
        isused[i] = 1
        arr.append(i)
        backtracking()
        arr.pop()
        isused[i] = 0

backtracking()