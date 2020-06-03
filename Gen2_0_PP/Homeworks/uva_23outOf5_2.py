def helperFunc(arr, result, j):
	if(result == 23 or j == len(arr)):
		return True
		
    for i in range(len(arr)):
		if(result == float('-inf')):
			temp = arr[i]
			arr[i] = -1
			ans = helperFunc(arr, temp, j + 1)
			arr[i] = temp
			if(ans):
				return True
			
		else:
			if(arr[i] != -1):
				temp = arr[i]
				arr[i] = -1
				ans = helperFunc(arr, result + temp, j + 1) or helperFunc(arr, result*temp, j + 1) or helperFunc(arr, result - temp, j + 1)
				arr[i] = temp
				if(ans):
					return True
	return False

while(True):
    arr = list(map(int, input().split()))
    if(arr[0] == 0):
		break

	if(helperFunc(arr, float('-inf'), 0)):
		print("Possible")

	else:
		print("Impossible")
