#arr = [2,4,12,5,7,24,6,3]


def fucSunlight(arr, i):
    global maxx, cntt
    if i >= len(arr):
        return
    if arr[i] > maxx:
        cntt+=1
        maxx = arr[i]
    fucSunlight(arr, i+1)

tCs = int(input())
while(tCs):
    maxx = 0
    cntt = 0
    tCs -= 1
    sz = int(input())
    arr = list(map(int,input().split()))
    fucSunlight(arr,0)
    print(cntt)