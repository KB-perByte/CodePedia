def indexOfFirstOne( arr, left, right): 
    if arr[0] == 1:
        return 0
    elif arr[right] == 0:
        return -1
        
    while (left <= right): 
        mid = int((left + right) / 2) 
        if (arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0)): 
            return mid 
        elif (arr[mid] == 1): 
            right = mid - 1

        else: 
            left = mid + 1
    return -1

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        print(indexOfFirstOne(a,1, n-1))