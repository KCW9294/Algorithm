def solution(nums):
    pick = len(nums)//2
    nums = set(nums)
    possible = len(nums)
    if pick>=possible:
        return possible
    else:
        return pick
