for x in range(t):
    a,b,c=map(int,input().split())
    n=int(input())
    new_arr=[]
    arr=list(map(int,input().split()))
    for i in arr:
        z=i*i*a+b*i+c
        new_arr.append(z)
    new_arr.sort()
    print((" ").join(str(p) for p in new_arr))
    