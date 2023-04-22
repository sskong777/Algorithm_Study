n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

def backtrack(cnt):
    if cnt == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        if nums[i] not in result:
            result.append(nums[i])
            backtrack(cnt+1)
            result.pop()

backtrack(0)
