#code
t = int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a=0
    b=n-1
    while arr[a]>arr[b]:
        temp_a=a
        temp_b=b
        while arr[temp_a]>arr[b]:
            temp_a+=1
        while arr[temp_b]<arr[a]:
            temp_b-=1
        if temp_a-a<b-temp_b:
            a+=1
        else:
            b-=1
    print(b-a)