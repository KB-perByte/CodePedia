class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        
        if n < 3:
            return 1
        
        def factorialCalc(num): 
            factorial = 1
            for i in range(1,num + 1):
                factorial = factorial*i
            return factorial
        
        def sOE(n, primes):
            mark = [False] * (n + 1)
            for i in range(2, int(math.sqrt(n)) + 1):
                if not mark[i]:
                    primes.append(i)
                    for j in range(i*2, n + 1, i):
                        mark[j] = True
            for i in range(int(math.sqrt(n))+1, n + 1):
                if not mark[i]:
                    primes.append(i)

            return primes

        _primes = list()
        _primes = sOE(n, _primes)
        #print(_primes)
        _composite = n - len(_primes)
        return (factorialCalc(len(_primes))*factorialCalc(_composite)) % (10**9 + 7)