from bisect import bisect,bisect_left,bisect_right

def toReach(arr, n):
    search = -1
    if n in arr:
        search = bisect(arr,n)
    if search == -1:
        high = bisect_right(arr,n)-1
        low = bisect_left(arr,n)+1
        l = n - arr[low]
        h = arr[high] - n
        if h<l:
            return h, high
        else:
            return l, low
    else:
        return 0, search

def getMinCost(crew_id, job_id):
    # Write your code here
    job_id.sort()
    tDist = 0
    for i in crew_id:
        dd ,l = toReach(job_id, i)
        #job_id[l] = -1
        tDist  += dd
    return tDist

pp = getMinCost([5,5,3,1,4,6], [5, 9, 8, 3, 15, 1])
print(pp)
