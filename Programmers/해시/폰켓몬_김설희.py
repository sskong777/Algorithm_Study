def solution(nums):

    kinds = len(list(set(nums)))
    standard = len(nums) // 2

    return standard if kinds > standard else kinds