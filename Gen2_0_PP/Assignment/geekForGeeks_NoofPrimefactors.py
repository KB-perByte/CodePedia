


def countPrimes(n):
        if n < 2:
            return 0    
        strikes = [1] * n       
        strikes[0] = 0
        strikes[1] = 0     
        for i in range(2, int(n**0.5)+1):
            if  strikes[i] != 0:
                #strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
                strikes[i*i:n:i] = [0] * len(strikes[i*i:n:i])
                #strikes[i*i:n:i] = i
        print (strikes)
        return sum(strikes)

print(countPrimes(101))



import math 
def primeFactors(n): 
    while n % 2 == 0: 
        print (2, end = ' ') 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            print (i, end = ' ') 
            n = n / i 
    if n > 2: 
        print (n, end = ' ') 

primeFactors(12246) 