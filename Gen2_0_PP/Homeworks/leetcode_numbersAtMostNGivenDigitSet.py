class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        N = str(N)
        lenN = len(N)
        result = sum(len(D) ** i for i in range(1, lenN)) 
        i = 0
        while i < len(N):
            result += sum(c < N[i] for c in D) * (len(D) ** (lenN - i - 1)) 
            if N[i] not in D: break  
            i += 1
        return result + (i == lenN)
            