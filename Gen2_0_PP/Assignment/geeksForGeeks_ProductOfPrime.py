#code
from math import floor, sqrt 
m = 1000000007

def _Sieve(limit, primes): 
    mark = [False]*(limit+1) 
      
    for i in range(2, limit+1): 
        if not mark[i]: 
            primes.append(i) 
            for j in range(i, limit+1, i): 
                mark[j] = True
 
def primesInRange(low, high): 
    limit = floor(sqrt(high)) + 1
    
    primes = list() 
    _Sieve(limit, primes) 
    res = 1
    n = high - low + 1
    mark = [False]*(n+1) 
    for i in range(len(primes)): 
        loLim = floor(low/primes[i]) * primes[i] 
        if loLim < low: 
            loLim += primes[i] 
        if loLim == primes[i]: 
            loLim += primes[i] 
        for j in range(loLim, high+1, primes[i]): 
            mark[j-low] = True
    for i in range(low, high+1): 
        if not mark[i-low]:
            res*=i
    print(res%m)
            #print(i, end = " ") 

for testcases in range(int(input())):
    numbers = list(map(int, input().split()))
    #print(numbers)
    n, r=numbers[0], numbers[1]
    primesInRange(n, r) 