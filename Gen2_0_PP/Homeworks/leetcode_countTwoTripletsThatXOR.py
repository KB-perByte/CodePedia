'''Count Triplets That Can Form Two Arrays of Equal XOR
'''

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = total = 0
        for r in range(len(arr)):
            total ^= arr[r]
            temp = total
            for l in range(r):
                if temp == 0:
                    res += r - l
                temp ^= arr[l]
        return res