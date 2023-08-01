dict = {}

def solution(nums):
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    answer = min(len(dict), len(nums) // 2)
    return answer