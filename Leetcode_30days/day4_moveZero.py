'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.'''
class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        count = 0 
        for i in range(n): 
            if arr[i] != 0: 
                arr[count] = arr[i] 
                count+=1

        while count < n: 
            arr[count] = 0
            count += 1
        return arr

                
