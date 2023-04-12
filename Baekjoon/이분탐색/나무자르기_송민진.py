import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))
trees.sort()

def check(mid):
    tmp_sum = 0
    for i in range(len(trees)):
        if trees[i] > mid:
            tmp_sum += trees[i] - mid
    return tmp_sum >= m

left, right = 0, max(trees)
mid = (left + right) // 2
answer = 0
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid
        answer = mid
    else:
        right = mid

print(answer)
