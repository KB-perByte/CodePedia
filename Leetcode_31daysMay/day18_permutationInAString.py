class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        subStr = [ord(x) - ord('a') for x in s1] 
        mainStr = [ord(x) - ord('a') for x in s2] #reference array taken just to evaluate the pos of occurance
        #as per ASCII
        
        target = [0] * 26
        for x in subStr:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(mainStr):
            window[x] += 1
            if i >= len(subStr):
                window[mainStr[i - len(subStr)]] -= 1
            if window == target:
                return True
        return False