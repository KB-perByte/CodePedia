import math 
MAX = 10000
primes = []
def Sieve(): 
	n = MAX 
	nNew = int(math.sqrt(n)) 
	marked = [0] * (int(n / 2 + 500))
	for i in range(1, int((nNew - 1) / 2) + 1): 
		for j in range(((i * (i + 1)) << 1), 
						(int(n / 2) + 1), (2 * i + 1)): 
			marked[j] = 1
	primes.append(2)
	for i in range(1, int(n / 2) + 1): 
		if (marked[i] == 0): 
			primes.append(2 * i + 1)

def binarySearch(left, right, n): 
	if (left <= right): 
		mid = int((left + right) / 2)
		if (mid == 0 or mid == len(primes) - 1): 
			return primes[mid]
		if (primes[mid] == n): 
			return primes[mid - 1]
		if (primes[mid] < n and primes[mid + 1] > n): 
			return primes[mid] 
		if (n < primes[mid]): 
			return binarySearch(left, mid - 1, n) 
		else: 
			return binarySearch(mid + 1, right, n)
	return 0

Sieve()
testCases = int(input())
while(testCases):
    testCases-=1
    n = int(input())
    print(binarySearch(0, len(primes) - 1, n))
