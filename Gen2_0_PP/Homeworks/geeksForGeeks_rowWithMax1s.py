def binarySearchRec(array, l, r, toSearch): 
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

testCases = int(input())
while(testCases):
    testCases-=1
    a = list(map(int,input().split()))
    binB = list(map(int,input().split()))
    
    def rowWithMax1s(binB , a):
        idx = 0
        idxl = a[1]
        ans = 0
        pos = a[1]

        if idx == 0 and idxl == 0:
            return -1

        for k in range(a[0]):
            
            if binB[idx:idxl][0] == 1:
                return k
            
            if pos == 0:
                return k-1

            x = indexOfFirstOne(binB[idx:idxl], 0, a[1]-1)
            
            if x < pos and x != -1:
                pos = x
                ans = k

            idxl+=a[1]
            idx+=a[1]
            
        return ans
    
    print(rowWithMax1s(binB, a))

