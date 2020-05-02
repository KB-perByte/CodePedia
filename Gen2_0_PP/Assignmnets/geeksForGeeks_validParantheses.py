# Python3 program to find valid 
# paranthesisations of length n 
# The majority of code is taken 
# from method 3 of 
# https:#www.geeksforgeeks.org/program-nth-catalan-number/ 

# Returns value of Binomial 
# Coefficient C(n, k) 
def binomialCoeff(n, k): 
	res = 1; 

	# Since C(n, k) = C(n, n-k) 
	if (k > n - k): 
		k = n - k; 

	# Calculate value of [n*(n-1)*--- 
	# *(n-k+1)] / [k*(k-1)*---*1] 
	for i in range(k): 
		res *= (n - i); 
		res /= (i + 1); 

	return int(res); 

# A Binomial coefficient based 
# function to find nth catalan 
# number in O(n) time 
def catalan(n): 
	
	# Calculate value of 2nCn 
	c = binomialCoeff(2 * n, n); 

	# return 2nCn/(n+1) 
	return int(c / (n + 1)); 

# Function to find possible 
# ways to put balanced parenthesis 
# in an expression of length n 
def findWays(n): 
	
	# If n is odd, not possible to 
	# create any valid parentheses 
	if(n & 1): 
		return 0; 

	# Otherwise return n/2'th 
	# Catalan Numer 
	return catalan(int(n / 2)); 

# Driver Code 
n = 6; 
print("Total possible expressions of length", 
					n, "is", findWays(6)); 
	
# This code is contributed by mits 
