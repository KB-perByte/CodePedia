import math

def isEven( n) :  
    if (n ^ 1 == n + 1) : 
        return True;  
    else : 
        return False; 

MAX = 1000001; 
factor = [0]*(MAX + 1); 

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime

primes = SieveOfEratosthenes(1000001)

n = int(input())
while(n):
    x, temp = 0, 0
    n-=1
    x = int(input())
    if isEven(x):
        temp = x//2
        print(temp, temp)
    else:
        if primes[x]:
            print(1, x-1)
        else:
            temp = x//2
            print(temp -1, (x-temp)+1) 



#try 2

 
t=int(input())
 
 
for i in range(t):
	
	n=int(input())
	if n%2==0:
		a=int(n/2)
		print(a,a)
	else:
		for x in range(3,10**5,2):
			
			if n%x==0:
				b=int(n*(x-1)/x)
				print(n-b,b)
				break
		else:
			print(x)
			print(1,n-1)
		
#try 3

t=int(input())
 
 
for i in range(t):
	
	n=int(input())
	if n%2==0:
		a=int(n/2)
		print(a,a)
	else:
		for x in range(3,10**5,2):
			
			if n%x==0:
				b=int(n*(x-1)/x)
				print(n-b,b)
				break
		else:
			print(1,n-1)


#try 4
import math

def isEven( n) :  
    if (n ^ 1 == n + 1) : 
        return True;  
    else : 
        return False; 

t = int(input())
while t!=0:
    t-=1
    n = int(input())
    if isEven(n):
        print(n//2,n//2)
    else:
        i=1
        p=1
        while i*i<n:
            if n%i==0:
                p = int(n//i)
            i+=1
        print(p,n-p)


#try 5
for j in range(int(input())):
    a = int(input())
    if a%2==  0:
        print(a//2, a//2) 
    else:
        for i in range(3,(a//2)+2, 2):
            if a%i==0:
                 print(a//i,a-(a//i))
                 break
            
            else:
                print(1, a-1)

#try 6

import math

def isEven( n) :  
    if (n ^ 1 == n + 1) : 
        return True;  
    else : 
        return False; 

t = int(input())
while t!=0:
    t-=1
    n = int(input())
    if isEven(n):
        print(n//2,n//2)
    else:
       for j in range(2,10**5, 2):
            if(n%j==0):
                print(n//j,n-n//j)
                break
            else:
                print(1,n-1)

#try 7
import math
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(2,int(math.sqrt(n)+2)):
        if(n%j==0):
            print(n//j,n-n//j)
            break
    else:
        print(1,n-1)