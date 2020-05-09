def binarySearch(array, l, r, toSearch):  # iterative one a wise choise easy to understand
    while l <= r: 
        mid = l + (r - l)//2
        if array[mid] == toSearch: 
            return mid 
        elif array[mid] < toSearch: 
            l = mid + 1
        else: 
            r = mid - 1
    return -1

def binarySearchRec(array, l, r, toSearch): #recusive and crazy approach 
    if r >= l: 
        mid = l + (r - l)//2
        if array[mid] == toSearch: 
            return mid 
        elif array[mid] > toSearch: 
            return binarySearchRec(array, l, mid-1, toSearch) 
        else: 
            return binarySearchRec(array, mid+1, r, toSearch)   
    else: 
        return -1