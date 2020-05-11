
def kthSmallest(arr, k, n):
    l = min(arr)
    h = max(arr)

    def countEle(matrix, md):
        cnt = 0
        for k in matrix:
            if k <= md:
                cnt += 1
        return cnt

    while(l <= h):
        m = (l+h)//2
        cnt = countEle(arr, m)
        if cnt < k: l=m+1
        else:
            cnt = countEle(arr, m)
            if cnt < k:
                return m
            else:
                h = m-1
        return h

if __name__ == "__main__" :  

    arr = [ 7, 10, 4, 3, 20, 15 ]
    n = len(arr)
    k = 3
    print(kthSmallest(arr, k, n))