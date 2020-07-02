
def printArray(A, size): 

	for i in range(size): 
		print(A[i], end = " ") 
	print() 

def merge(arr, l, m, r): 
	i, j, k = 0, 0, 0
	n1 = m - l + 1
	n2 = r - m 

	L = [arr[l + i] for i in range(n1)] 
	R = [arr[m + 1 + j] for j in range(n2)] 

	
	i = 0 # Initial index of first subarray 
	j = 0 # Initial index of second subarray 
	k = l # Initial index of merged subarray 
	while (i < n1 and L[i] < 0): 
		arr[k] = L[i] 
		k += 1
		i += 1

	while (j < n2 and R[j] < 0): 
		arr[k] = R[j] 
		k += 1
		j += 1

	while (i < n1): 
		arr[k] = L[i] 
		k += 1
		i += 1

	while (j < n2): 
		arr[k] = R[j] 
		k += 1
		j += 1

def RearrangePosNeg(arr, l, r): 

	if(l < r): 
		m = l + (r - l) // 2
		RearrangePosNeg(arr, l, m) 
		RearrangePosNeg(arr, m + 1, r) 
		merge(arr, l, m, r) 
	
arr = [ -12, 11, -13, -5, 
		6, -7, 5, -3, -6 ] 
arr_size = len(arr) 

RearrangePosNeg(arr, 0, arr_size - 1) 

printArray(arr, arr_size) 

