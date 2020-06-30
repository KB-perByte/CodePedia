arr = [1, 4, 45, 6, 10, 8]
k = 16

arr.sort() #[1,4,6,8,10,45]
i = 0
j = len(arr)-1 
cnt = 0
while(i<j):
    print(i,j)
    if(arr[i] + arr[j] == k):
        cnt+=1
        break
    elif( arr[i] + arr[j] > k):
        j-=1
    else:
        i+=1
print(cnt)

def check(arr, k):
        arr.sort()
        i = 0
        j = len(arr) - 1
        while(i<j):
            if(arr[i] + arr[j] == k):
                return True
            elif(arr[i] + arr[j] > k):
                j-=1
            else:
                i+=1

n = int(input())
while(n):
    n-=1
    par = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    if check(arr, par[1]):
        print('Yes')
    else:
        print('No')

print(cnt)