'''subsequences-size-three-array-whose-sum-divisible-m'''
# Python program to find count of 
# subsequences of size three 
# divisible by M. 

def coutSubSeq(A, N,M) : 
	sum = 0
	ans = 0

	# Three nested loop to find all the 
	# sub sequences of length three in 
	# the given array A[]. 
	for i in range(0, N) : 
		for j in range(i + 1, N) : 
			for k in range(j + 1, N) : 
				sum = A[i] + A[j] + A[k] 

				# checking if the sum of 
				# the chosen three number 
				# is divisible by m. 
				if (sum % M == 0) : 
					ans = ans + 1
	return ans 
	
# Driver code 
M = 3
A = [ 1, 2, 4, 3 ] 
N = len(A) 
print coutSubSeq(A, N, M) 

# This code is contributed by Nikita Tiwari. 
