def _gcd(x, y): 
    
    while(y): 
        x, y = y, x % y 
    return x 
        
def calc(arr, n):
    op = 0 
    for i in range(n-1): 
        gcd = _gcd(arr[i], arr[i+1]) 
        for j in range(2,int(gcd+1)):
            if arr[i]%j == 0 and arr[i+1]%j == 0:
                op+=1
                while(arr[i+1]%j ==0):
                    arr[i+1]/=j 

    return op

lenAr = int(input())
arr = list(map(int, input().rstrip().split()))
print(calc(arr, lenAr))