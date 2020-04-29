
MAX = 1000001; 
factor = [0]*(MAX + 1); 

def generateSmallestPrimeFactors(): 
    factor[1] = 1
    for i in range(2,MAX): 
        factor[i] = i

    for i in range(4,MAX,2): 
        factor[i] = 2

    i = 3
    while(i * i < MAX): 
        if (factor[i] == i): 
            j = i * i
            while(j < MAX):  
                if (factor[j] == j): 
                    factor[j] = i
                j += i
        i+=1
    return factor

print(generateSmallestPrimeFactors())

        
