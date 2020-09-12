#User function Template for python3

##Structure of node
'''
# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
'''
##Complete this function
def getCountOfNode(root,low,high):
    ##Your code here
    if root == None: 
        return 0
          
    # Special Optional case for improving  
    # efficiency  
    if root.data == high and root.data == low:  
        return 1
  
    # If current node is in range, then  
    # include it in count and recur for  
    # left and right children of it  
    if root.data <= high and root.data >= low:  
        return (1 + getCountOfNode(root.left, low, high) + 
                    getCountOfNode(root.right, low, high)) 
  
    # If current node is smaller than low,  
    # then recur for right child  
    elif root.data < low:  
        return getCountOfNode(root.right, low, high) 
  
    # Else recur for left child  
    else: 
        return getCountOfNode(root.left, low, high)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root
    

    
def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
            
        lr=[int(x) for x in input().strip().split()]

        print(getCountOfNode(root,lr[0],lr[1]))
        testcases-=1

if __name__=="__main__":
    main()
# } Driver Code Ends