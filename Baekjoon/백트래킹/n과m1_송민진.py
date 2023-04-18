# 풀이 1 - 임시
from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
answer = list(permutations(arr, m))

for ans in answer:
    print(*ans)