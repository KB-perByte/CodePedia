#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
def maxLen(arr, N):
    # code here
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1
    HM = {}
    maxLen = 0
    summ = 0
    
    for i in range(len(arr)): 
        summ += arr[i] 
        
        if summ is 0: 
            maxLen = i + 1
  
        if summ in HM: 
            maxLen = max(maxLen, i - HM[summ] ) 
        else: 
            HM[summ] = i 
  
    return maxLen 


#{ 
#  Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=maxLen(a, len(a))
    print(s)
# } Driver Code Ends