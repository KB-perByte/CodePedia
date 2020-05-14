import random
def findSingleElement(nums):
    l , r , n = 0, len(nums)-1 , len(nums)
    while l < r:
        mid = (l + r) //2
        if mid % 2 == 1:
            mid -= 1
        if mid + 1 == n or nums[mid + 1] != nums[mid]:
            r = mid
        else:
            l = mid + 2
    print(nums[l])
    return nums[l]

x = [1,1,2,3,3,4,4,8,8]
findSingleElement(x)

def getRandomInRange(l,r):
    return random.randint(l,r)

def randomSearch(numArr, k):
    l = 0
    r = len(numArr)-1
    while l < r:
        idx = getRandomInRange(l,r)
        if numArr[idx] == k:
            return idx
        elif numArr[idx] >= k:
            r = idx
        elif numArr[idx] <= k:
            l = idx
    return -1 

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(randomSearch(x, 12))
