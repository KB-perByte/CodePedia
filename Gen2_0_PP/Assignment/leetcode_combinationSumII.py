class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # let's enforce the ascending order so the function below can rely on it
        candidates.sort()
        
        # let's find all unique subsequences summing up to the given target
        return self.find_subsequences(candidates, target)
        
        
    def find_subsequences(self, candidates, target):
        'will return the list of possible unique subseqneces summing up to target'
        results = []
        
        for i, cnd in enumerate(candidates):
            if i > 0 and cnd == candidates[i-1]:
                # this will only produce duplicates so let's move on
                continue
                
            if cnd < target:
                # there's a chance that we'll find something, so let's try to solve a smaller problem
                subs = self.find_subsequences(candidates[i+1:], target - cnd)
                # if we found something let's prefix that with the current candidate and add to results
                for sub in subs:
                    results.append([cnd] + sub)
            elif cnd == target:
                # we found a perfect match
                results.append([cnd])
                break # all the following ones are either equal 
            else:
                break # or higher which is not what we're interested in
        
        return results