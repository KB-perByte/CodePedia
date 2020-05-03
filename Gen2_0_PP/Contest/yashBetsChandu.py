def makeCombinations(str):
    length, n= len(str) , 0
    print(length)
    for i in range(2, length):
        if length%i == 0:
            n=length//i
            break
    if n==0:
        print("-1")
        return

    chars = int(length/n)
    equalStr = []
    if(length % n != 0):  
            print("-1")
    else:  
        for i in range(0, length, chars):  
            part = str[ i : i+chars] 
            equalStr.append(part)    
        for i in equalStr:  
            print(i) 
            
_str = input()
makeCombinations(_str)