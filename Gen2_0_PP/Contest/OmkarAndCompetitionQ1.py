for i in range(int(input())):
    n=int(input())
    print("1 "*n)


#try 2
for x in range(int(input())) : 
    print(*[x if x<1000 else x-1000 for x in range(1,int(input())*2,2)] )