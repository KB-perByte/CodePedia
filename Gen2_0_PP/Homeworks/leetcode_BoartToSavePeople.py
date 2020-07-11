class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 0: return 0
        
        people.sort()
        
        left, right = 0, len(people) - 1
        
        ret = 0
        while left <= right:
            if people[right] + people[left] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            ret += 1
            
        return ret