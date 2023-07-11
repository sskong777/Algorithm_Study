def solution(nums):
    kind = set(nums)
    total = len(nums) / 2
    if len(kind) >= total:
        return total
    else:
        return len(kind)
    return answer