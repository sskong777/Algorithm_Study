# 풀이 1 - itertools 활용
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
answer = 0
coms = list(map(list, permutations(arr, n)))

for com in coms:
    tmp_sum = 0
    for i in range(1, n):
        tmp_sum += abs(com[i-1] - com[i])
    answer = max(answer, tmp_sum)

print(answer)

# 풀이 2 - 백트랙킹
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
answer = 0
visited = [False] * n

def backtracking(tmp_list):
    global answer

    if len(tmp_list) == n:
        tmp_sum = 0
        for i in range(1, n):
            tmp_sum += abs(tmp_list[i-1] - tmp_list[i])
        answer = max(tmp_sum, answer)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            tmp_list.append(arr[i])
            backtracking(tmp_list)
            visited[i] = False
            tmp_list.pop()

backtracking([])

print(answer)