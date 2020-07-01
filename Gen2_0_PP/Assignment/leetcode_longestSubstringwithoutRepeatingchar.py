class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans,n,i,j=0,len(s),0,0
        Set = set()
        while i<n and j<n:
            if s[j] not in Set:
                Set.add(s[j]) #if character is unique add to set
                j+=1
                ans=max(ans,j-i) #maximize the length (i,j)
            else:
                Set.remove(s[i]) #if character isn't unique remove from set
                i+=1 #reduce the interval length
        return ans