n, k = map(int, input().split())
nums = list(range(2, n+1))
kth_removed = 0

for i in range(2, n+1):
    if i not in nums:
        continue
    for j in range(i, n+1, i):
        if nums.count(j) == 0:
            continue
        kth_removed += 1
        if kth_removed == k:
            print(j)
            break
        nums.remove(j)
    if kth_removed == k:
        break
