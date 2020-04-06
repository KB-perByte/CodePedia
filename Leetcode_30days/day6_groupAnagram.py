'''Given an array of strings, group anagrams together.'''

from collections import defaultdict
class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        hashMap = defaultdict(list)      
        for wrd in strs:   
            value = wrd        
            key = list(wrd)
            key.sort()
            hashMap[str(key)].append(wrd)
        results = []  
        for key in hashMap.keys(): 
            results.append(hashMap[key])
        return results
     
