def _gcd(x, y): 
    
    while(y): 
        x, y = y, x % y 
    return x 
        
def calc(arr, n):
    num1 = arr[0] 
    num2 = arr[1] 
    gcd = _gcd(num1, num2) 

    for i in range(2, n): 
        gcd = _gcd(gcd, arr[i]) 

    return gcd

lenAr = int(input())
arr = list(map(int, input().rstrip().split()))
print(calc(arr, lenAr))