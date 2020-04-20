#Assignment (Arrays 1)

'''https://leetcode.com/submissions/detail/327166427/'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        w, lvl, lt, rt = 0, 0, 0, len(height)-1
        while lt < rt:
            if height[lt] < height[rt]:
                l = height[lt]
                lt += 1
            else:
                l = height[rt]
                rt -= 1

            lvl = max(lvl, l)          
            w += lvl - l

        return w
#debugs =)
def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        w, lvl, lt, rt = 0, 0, 0, len(height)-1
        while lt < rt:
            if height[lt] < height[rt]:
                l = height[lt]
                lt += 1
            else:
                l = height[rt]
                rt -= 1

            lvl = max(lvl, l)          
            w += lvl - l

        return w

trap([0,1,0,2,1,0,1,3,2,1,2,1])