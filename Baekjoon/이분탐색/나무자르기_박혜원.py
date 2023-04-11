# [2805] 나무자르기

# 나무의 수 N
# 집으로 가져가려고 하는 나무의 길이 M
# 나무 길이들 heights

n, m = map(int, input().split())
tree_heights = list(map(int, input().split()))

start, end = 0, max(tree_heights)

while start <= end:
    total = 0
    # 절단기 높이 지정 : mid
    mid = (start + end) // 2

    for tree in tree_heights:
        if tree > mid:
            total += tree - mid
    # 잘라낸 떡의 양이 부족한 경우(더 많이 잘라내야됨 = left 탐색)
    # 절단기 높이를 낮춤
    if total < m:
        end = mid - 1
    # 잘라낸 떡의 양이 충분한 경우(덜 잘라내야됨 = right 탐색)
    # 절단기 높이를 높임
    else:
        answer = mid
        start = mid + 1

# 절단기에 설정할 수 있는 최대 mid값
print(answer)
