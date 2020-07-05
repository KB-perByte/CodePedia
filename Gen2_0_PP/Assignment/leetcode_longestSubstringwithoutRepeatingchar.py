class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans,n,x,y=0,len(s),0,0
        arr = set()
        while x<n and y<n:
            if s[y] not in arr:
                arr.add(s[y]) 
                y+=1
                ans=max(ans,y-x) 
            else:
                arr.remove(s[x]) 
                x+=1 
        return ans