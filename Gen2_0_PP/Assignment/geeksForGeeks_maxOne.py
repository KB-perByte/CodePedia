def maxOnes(input): 
    result = list(map(sum,input)) 
    print (result.index(max(result))) 

# Driver program 
if __name__ == "__main__": 
    input = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]] 
    maxOnes(input) 