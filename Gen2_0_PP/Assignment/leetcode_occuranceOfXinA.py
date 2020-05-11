def count(arr, x, n): 
    i = first(arr, 0, n-1, x, n) 
    if i == -1: 
        return i  
    j = last(arr, i, n-1, x, n)
    return j-i+1


def first(arr, low, high, x, n): 
    mid = 0
    if high >= low: 
        mid = (low + high)//2      
    if (mid == 0 or x > arr[mid-1]) and arr[mid] == x: 
        return mid 
    elif x > arr[mid]: 
        return first(arr, (mid + 1), high, x, n) 
    else: 
        return first(arr, low, (mid -1), x, n) 
    return -1

def last(arr, low, high, x, n): 
    mid = 0
    if high >= low: 
        mid = (low + high)//2
    if(mid == n-1 or x < arr[mid+1]) and arr[mid] == x : 
        return mid 
    elif x < arr[mid]: 
        return last(arr, low, (mid -1), x, n) 
    else: 
        return last(arr, (mid + 1), high, x, n)      
    return -1



for i in range(int(input())):
    xn = list(map(int, input().rstrip().split()))
    arr = list(map(int, input().rstrip().split()))
    x = xn[1]  
    n = len(arr) 
    print(count(arr, x, n))