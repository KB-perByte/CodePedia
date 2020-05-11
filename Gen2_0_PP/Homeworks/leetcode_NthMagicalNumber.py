import math
class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        lcm= A*B // math.gcd(A,B)
        l,r=2,10**14
        while l<=r:
            mid=(l+r)//2
            n = mid//A+mid//B-mid//lcm
            if n>=N:
                r=mid-1
           
            else:
                l=mid+1
        return l%(10**9+7)