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

generateSmallestPrimeFactors()

def primeFactors(xx):
    factList = []
    while(xx != 1):
        factList.append(factor[int(xx)])
        xx /= factor[int(xx)]
    return factList

li= [6060, 24, 16 ,404, 77, 88, 1005, 20002] 

def myTestCase(li):
    for i in li:
        print("Factors of ", i)
        print(primeFactors(i))

myTestCase(li)


# [3, 2, 2, 2] 24
# [2, 2, 2, 2] 16
# [2, 2, 101] 404
# [7, 11] 77
# [2, 2, 2, 11] 88
# [5, 3, 67] 1005
# [137, 2, 73] 20002

