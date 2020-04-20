'''https://leetcode.com/submissions/detail/327192198/'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ''' #the bad code =) 
        for i in range(0,k):
            ele= nums.pop()
            nums.insert(0,ele)
        '''
        
        k %= len(nums)
        if k == 0:
            return
    
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]