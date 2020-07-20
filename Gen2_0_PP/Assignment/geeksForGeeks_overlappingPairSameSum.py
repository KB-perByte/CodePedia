def findPairs(arr, size): 
	Map = {} 
	for i in range(0, size - 1): 
		for j in range(i + 1, size): 
			Sum = arr[i] + arr[j] 
			if Sum in Map: 
				for pair in Map[Sum]: 
					m, n = pair 
					if ((m != i and m != j) and
						(n != i and n != j)): 
						
						print("Pair First ({}, {})". 
							format(arr[i], arr[j])) 
						print("Pair Second ({}, {})". 
							format(arr[m], arr[n])) 
						return
			
			if Sum not in Map: 
				Map[Sum] = [] 
			Map[Sum].append((i, j)) 
	print("No such non-overlapping pairs present") 

if __name__ == "__main__": 
	arr = [8, 4, 7, 8, 4] 
	size = len(arr) 
	findPairs(arr, size) 
	

