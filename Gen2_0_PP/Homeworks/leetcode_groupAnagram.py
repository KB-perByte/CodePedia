class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict ={}
        for n in strs:
            string = ''.join(sorted(n))
            if string in anag_dict:
                anag_dict[string].append(n)
            else:
                anag_dict[string] = [n]
				     
        ans = anag_dict.values()
        return ans   