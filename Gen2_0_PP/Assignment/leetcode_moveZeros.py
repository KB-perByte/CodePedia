
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos_num = 0
        curr = 0
        while curr<len(nums):
            if nums[curr] != 0:
                nums[pos_num],nums[curr] = nums[curr],nums[pos_num]
                pos_num+=1
            curr+=1
        return nums
        