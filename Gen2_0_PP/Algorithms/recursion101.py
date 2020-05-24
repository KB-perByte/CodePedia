def printFun(test): 
  
    if (test < 1): 
        return
    else: 
      
        print( test, end = " ") 
        printFun(test-1) # statement 2 
        print( test, end = "_") 
        return

test = 3
printFun(test) 