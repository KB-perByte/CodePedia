def checkSum(arr, j, k):
    for x in range(j):
        if k == 0 :
            return True
        else:
            k = 0
        for y in range(x, j):
            k += arr[y]
            print(k , end = ' ')
            if k == 0:
                print(True)
                break
    print(False)
    return
    
n = int(input())
while(n):
    n-=1
    par = int(input())
    arr = list(map(int,input().split()))

    checkSum(arr, par, 0)

#imp2

def SubArrayOfZeroSum(L):
    sum=0
    s=set()
    for i in range(len(L)):
        sum+=L[i]
        
        if sum==0 or sum in s:
            return "Yes"
        s.add(sum)
        
    return "No"

if __name__=='__main__':
    T=int(input())
    for i in range(T):
        l=int(input())
        A=list(input().split())
        L=[int(i) for i in A]

        result=SubArrayOfZeroSum(L)
        print(result)