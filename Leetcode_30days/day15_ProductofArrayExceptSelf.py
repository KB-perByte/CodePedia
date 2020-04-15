'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
'''
'''this would break for timelimit '''
def productExceptSelf(nums):
    lnums = len(nums)
    resArr = []
    for i in range(lnums):
        mul = 1
        for j in range(lnums):
            if i != j:
                mul = mul * nums[j]
        resArr.append(mul)
    return resArr
