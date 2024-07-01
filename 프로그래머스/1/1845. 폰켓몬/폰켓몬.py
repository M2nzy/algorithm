def solution(nums):
    answer = 0
    aLen = len(nums)//2
    nums = set(nums)
    bLen = len(nums)
    if aLen <= bLen:
        answer = aLen
    else:
        answer = bLen
    return answer