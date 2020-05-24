#code
# [2,3]
# [0] [2] [3] [5]

# [2,4,5]
# [] [2] [4] [5] [2,4] [4,5] [2,4,5]
# [0] [2] [4] [5] [6] [9] [11]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def recSubsets(nums,res,start,end,lst):
            #print('x')
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
    ans = []
    testcases-=1
    _ = input()
    arr = list(map(int, input().split()))
    for c in sl.subsets(arr): ans.append(sum(c))
    ans.sort()
    for c in ans: print(c , end = ' ' )
    #print(sum(c), end =' ')
    print()
    

# your code goes here