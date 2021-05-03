def solution(s):
    nums = eval(s[1:-1])
    if len(nums) > 1:
        nums = sorted(nums, key = len)
    else:
        return list(nums)
    result = []
    for num in nums:
        for n in num:
            if n not in result:
                result.append(n)
    return result
