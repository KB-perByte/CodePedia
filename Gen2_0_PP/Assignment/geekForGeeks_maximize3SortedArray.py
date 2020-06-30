
def solve(A, B, C): 
		i = len(A) - 1
		j = len(B) - 1
		k = len(C) - 1

		min_diff = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k])) 

		while i != -1 and j != -1 and k != -1: 
			current_diff = abs(max(A[i], B[j], 
			C[k]) - min(A[i], B[j], C[k])) 

			if current_diff < min_diff: 
				min_diff = current_diff 

			max_term = max(A[i], B[j], C[k]) 

			if A[i] == max_term: 
				i -= 1
			elif B[j] == max_term: 
				j -= 1
			else: 
				k -= 1
		return min_diff 

A = [ 5, 8, 10, 15 ] 
B = [ 6, 9, 15, 78, 89 ] 
C = [ 2, 3, 6, 6, 8, 8, 10 ] 
print(solve(A, B, C)) 
