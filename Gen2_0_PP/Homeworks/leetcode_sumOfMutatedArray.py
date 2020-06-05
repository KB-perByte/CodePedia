class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        s, n = 0, len(arr)
        
        for i in range(n):
            ans = round((target - s)/n)
            if ans <= arr[i]: return ans 
            s += arr[i]
            n -= 1
            
        return arr[-1]