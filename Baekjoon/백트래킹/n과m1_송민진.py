# 풀이 1 - 조합
from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
answer = list(permutations(arr, m))

for ans in answer:
    print(*ans)

# 풀이 2 - 백트랙킹
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
visited = [False] * (n+1)
answer = []

def solution(cnt, tmp):
    if cnt == m:
        print(*tmp)
        return

    for j in range(1, n+1):
        if visited[j] == False:
            visited[j] = True
            solution(cnt + 1, tmp+[j])
            visited[j] = False

solution(0, [])