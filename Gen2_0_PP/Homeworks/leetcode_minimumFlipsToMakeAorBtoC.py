class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        #considering 32 bit representation
        for i in range(32):
           
            
            bitA,bitB,bitC = (a>>i)&1, (b>>i)&1, (c>>i)&1
            print(i, bitA,bitB,bitC)
            #conditions
            if(bitA==1 and bitB==1 and bitC==0):
                result+=2
            elif((bitA==1 and bitB==0) and bitC==0):
                result+=1
            elif((bitA==0 and bitB==1) and bitC==0):
                result+=1
            elif((bitA==0 and bitB==0) and bitC==1):
                result+=1
        return result

s = Solution()
s.minFlips(2,6,5)



class Solution2:
    def minFlips(self, a: int, b: int, c: int) -> int: 
        flips = 0# SETUP THE NUMBER OF FLIPS NEEDED
        while (a | b) != c:# LOOP TILL CRITERIA OF (A OR B == C) IS MET
            print('xxxx')
            lsb_a, lsb_b, lsb_c = a & 1, b & 1, c & 1# GET LSB OF ALL 3 NUMBERS
            # CASE 1 : LSB(C) = 0 --> WE NEED LSB(A) = LSB(B) = 0
            if lsb_c == 0:
                flips += (lsb_a & 1) + (lsb_b & 1)
            # CASE 2 - LSB(C) = 1 --> WE NEED LSB(A) = 0 OR LSB(B) = 0
            else:
                flips += 1 ^ (lsb_a | lsb_b) 
            # RIGHT SHIFT ALL 3 NUMS
            a >>= 1; b >>= 1; c >>= 1
        # RETURN THE NUMBER OF FLIPS NEEDED
        return flips


s = Solution2()
s.minFlips(2,6,5)