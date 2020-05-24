class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def f(candidates, tot, tmp):
            
            if tot < target:
                for i, n in enumerate(candidates):
                    f(candidates[i:], tot + n, tmp + [n])
                    
            elif tot == target:
                ans.append(list(tmp))
                
        f(candidates, 0, [])
        return ans