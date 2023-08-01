def solution(nums):
    poketmon = set(nums)

    if(len(poketmon) > (len(nums))//2):
        return len(nums)//2
    return len(poketmon)