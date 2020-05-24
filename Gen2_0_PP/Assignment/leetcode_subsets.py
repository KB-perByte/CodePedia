class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def recSubsets(nums,res,start,end,lst):
            print('x')
            res.append(lst)
            if start == end:
                return
            for i in range(start,end):
                recSubsets(nums,res,i+1,end,lst+[nums[i]])
        recSubsets(nums,res,0,len(nums),[])      
        return res

sl = Solution()
testcases = int(input())
while(testcases):
    testcases-=1
    print(sl.subsets([2,4,5]))
    
