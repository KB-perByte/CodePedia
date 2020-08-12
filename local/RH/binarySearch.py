def binarySearch(arr, target, low, high):
    while low <= high:
        print(low,high)
        mid = (high+low)//2 
        if target == arr[mid]:
            return mid, True
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, False


def binarySearchRec(arr, target, low, high):
    if low > high:
        return -1, False
    else:
        mid = (low + (high - low))//2 
        if target == arr[mid]:
            return mid, True
        elif target  <  arr[mid]:
            return binarySearchRec(arr, target, low, high-1)
        else:
            return binarySearchRec(arr, target, low+1, high)


arr = [0,1,2,3,4,5,6,7,8,9]
N = 10
print(binarySearch(arr, 10, 0, N-1))
print(binarySearchRec(arr, 5, 0, N-1))