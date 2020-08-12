_sum = 0

def lSum(arr, n):
    global _sum
    if n < 0:
        return _sum
    _sum += arr[n]
    return lSum(arr, n-1)

arr = [1,2,3,4,5]
arr = []
N = len(arr)-1
print(lSum(arr, N))



