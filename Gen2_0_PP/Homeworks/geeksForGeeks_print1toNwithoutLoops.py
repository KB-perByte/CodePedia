def func(n,x):
    x+=1
    print(n ,x)
    if n == 1:
        return
    func(n-1,x)

func(10,0)


def printNos(n): 
	if n > 0: 
		printNos(n - 1) 
		print(n, end = ' ') 
 
printNos(100) 


