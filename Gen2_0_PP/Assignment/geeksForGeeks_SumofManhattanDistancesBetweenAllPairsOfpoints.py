 
def distancesum (x, y, n): 
	sum = 0
	# for each point, finding distance 
	# to rest of the point 
	for i in range(n): 
		for j in range(i+1,n): 
			sum += (abs(x[i] - x[j]) +
						abs(y[i] - y[j])) 
	
	return sum

# Driven Code 
x = [ -1, 1, 3, 2 ] 
y = [ 5, 6, 5, 3 ] 
n = len(x) 
print(distancesum(x, y, n) ) 
#approach 2
def distancesum (arr, n): 
	
	# sorting the array. 
	arr.sort() 
	res = 0
	sum = 0
	for i in range(n): 
		res += (arr[i] * i - sum) 
		sum += arr[i] 
	
	return res 
	
def totaldistancesum( x , y , n ): 
	return distancesum(x, n) + distancesum(y, n) 
	
# Driven Code 
x = [ -1, 1, 3, 2 ] 
y = [ 5, 6, 5, 3 ] 
n = len(x) 
print(totaldistancesum(x, y, n) ) 


