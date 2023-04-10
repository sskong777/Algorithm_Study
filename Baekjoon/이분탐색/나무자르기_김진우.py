n, m = map(int,input().split())
# n : 나무의수
# m : 집으로 가져가려고 하는 나무의 길이
# 4 ,7
trees = list(map(int,input().split()))
# 20 15 10 17

min_tree ,max_tree = 0, max(trees)
while min_tree <= max_tree :
    mid_tree = (min_tree + max_tree)//2
    ans = 0
    for i in trees:
        if i > mid_tree:
            ans += i - mid_tree
    print(f'min : {min_tree}, max : {max_tree} , mid : {mid_tree} , ans : {ans}')
    if ans >= m :
        min_tree = mid_tree + 1
    else:
        max_tree = mid_tree - 1

print(max_tree)