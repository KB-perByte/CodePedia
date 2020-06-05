class Solution:
    def __init__(self, w: List[int]):
        s = sum(w)
        self.weight = [w[0]/s]
        for i in range(1, len(w)):            
            self.weight.append(self.weight[-1]+w[i]/s)

    def pickIndex(self) -> int:
        l, r, seed = 0, len(self.weight)-1, random.random()
        while l < r:
            m = (l+r)//2
            if self.weight[m] <= seed: l = m+1
            else: r = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


class Solution2:

    def __init__(self, w: List[int]):
        self.prefixSum = []
        total = 0
        for i in w:
            total += i
            self.prefixSum.append(total)
        
    def pickIndex(self) -> int:
        rnd = random.uniform(0, 1) * self.prefixSum[-1]
        l, h = 0, len(self.prefixSum)-1
        while l < h:
            m = l + (h - l)//2 
            if rnd > self.prefixSum[m]:
                l = m + 1
            else:
                h = m
        return l
    
    
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()