
def GCD(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 

for T in range(int(input())):
    n = int(input())
    #divs = list(input().split())
    divs = list(map(int,input().split()))
    gcd = divs[0]
    for i in divs:
        gcd = GCD(gcd, int(i))
        if gcd == 1:
            break
    if gcd == 1:
        print(1)
    else:
        print(0)
    #print(gcd)