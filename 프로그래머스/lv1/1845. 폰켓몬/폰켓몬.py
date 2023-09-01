def solution(nums):
    pick = len(nums)/2
    possible = set(nums)
    if pick >= len(possible):
        return len(possible)
    else:
        return pick
