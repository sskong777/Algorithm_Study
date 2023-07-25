def solution(nums):
    # https://liveloper-jay.tistory.com/138
    ret = ''
    nums = list(map(str, nums))
    nums = sorted(nums, key=lambda x: x * 3, reverse=True)
    # nums = sorted(nums, key=lambda x: x * (10 ** (4-len(str(x)))), reverse=True)
    for i in nums:
        ret += i
    return str(int(ret))
