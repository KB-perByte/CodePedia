
import math 

def sumOfDigitsFrom1ToN(n) : 
	if (n<10) : 
		return (n*(n+1)/2) 
	d = (int)(math.log10(n)) 
	a = [0] * (d + 1) 
	a[0] = 0
	a[1] = 45
	for i in range(2, d+1) : 
		a[i] = a[i-1] * 10 + 45 * (int)(math.ceil(math.pow(10,i-1))) 
	p = (int)(math.ceil(math.pow(10, d))) 
	msd = n//p 
	return (int)(msd * a[d] + (msd*(msd-1) // 2) * p +
		msd * (1 + n % p) + sumOfDigitsFrom1ToN(n % p)) 

def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

t = int(input())
while(t):
    t-=1
    arr = []
    arr = list(map(int,input().split()))
    a = compute_hcf(arr[0], arr[1])
    _a = sumOfDigitsFrom1ToN(a)
    _a1 = sumOfDigitsFrom1ToN(arr[0])

    # if int(_a1 - _a) == 0:
    #     print(int(arr[1]))
    # else:
    print((int(_a1 - _a)-1)+int(arr[1]))





