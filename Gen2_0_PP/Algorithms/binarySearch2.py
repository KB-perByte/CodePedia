a = [12,14,15,16,17,19,23,245,356,868,969]


def binSearch(arr, element):
    left = 0
    right = len(arr)-1
    while left <= right:
        print("val of  l %d", left)
        print("val of  r %d", right)        
        middle = (left + right) // 2
        if arr[middle] == element:
            return middle
        elif arr[middle] < element:
            left = middle + 1 
        else:
            right = middle - 1

#print(binSearch(a,969))


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

def binSearch2D(arr, element):
    left = 0
    right = len(arr)-1
    while left <= right:
        print("val of  left ", left)
        print("val of  right ", right)        
        middle = (left + right) // 2
        if arr[middle][0] == element:
            return middle
        elif arr[middle][0] < element:
            left = middle + 1 
        else:
            right = middle - 1
    return -1, right

print(binSearch2D(matrix,7))

def searchmatrix2D(matrix, target):
    res = False
    row = len(matrix)
    if row < 1:
        return res
    
    col = len(matrix[0])
    if col < 1:
        return res
    
    if (target < matrix[0][0]) or (target > matrix[-1][-1]):
        return res
    
    low, high = 0, row * col
    while low < high:
        middle = low + (high - low) // 2
        n = matrix[middle // col][middle % col]
        if n > target:
            high = middle
        elif n < target:
            low = middle + 1
        else:
            return True
    return res