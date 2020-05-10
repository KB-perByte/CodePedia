def cowsFn(mid, arr, c): #O(n)
    count = 1
    curr = 0
    for i in range(1,n):
        if arr[i] - arr[curr] >= mid:
            count += 1
            curr = i
            if count >= c:
                return True
    return False

tCases = int(input())
while tCases: #log(h-l)
    n, c = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))

    arr.sort()

    l = 0
    h = arr[n-1]
    while l < h:
        mid = l + (h-l+1)//2
        num = cowsFn(mid, arr, c)
        if num:
            l = mid
        else:
            h = mid - 1
    print(l)
    tCases-=1


'''tagged most efficient one in internet '') '''

import sys
from time import time
from bisect import bisect_left as bl
from collections import defaultdict as ddict
from collections import deque as queue
from array import array
import heapq as heap
import math
 
def read(typ=str):
    return list(map(typ,sys.stdin.readline().split()))
 
def valid(arr,val,cnt):
    k = 1
    st = arr[0]
    for i in range(len(arr)):
        if arr[i] - st >= val:
            k+=1
            st = arr[i]
            if k >= cnt:
                return True
    return False
 
def main():
    t = read(int)[0]
    for _ in range(t):
        n,c = read(int)
        arr = [read(int)[0] for j in range(n)]
        arr.sort()
        h = arr[len(arr)-1]
        l = 1
        ans = 0
        while l < h:
            mid = l + (h-l)//2
            if valid(arr,mid,c):
                ans = mid
                l = mid + 1
            else:
                h = mid
        print(ans)