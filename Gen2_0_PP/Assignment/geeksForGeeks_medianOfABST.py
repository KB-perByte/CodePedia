#User function Template for python3
def counNodes(root): 
  
    # Initialise count of nodes as 0 
    count = 0
  
    if (root == None): 
        return count 
  
    current = root 
    while (current != None): 
      
        if (current.left == None): 
          
            # Count node if its left is None 
            count+=1
  
            # Move to its right 
            current = current.right 
          
        else:      
            """ Find the inorder predecessor of current """
            pre = current.left 
  
            while (pre.right != None and 
                    pre.right != current): 
                pre = pre.right 
  
            """ Make current as right child of its 
            inorder predecessor """
            if(pre.right == None): 
              
                pre.right = current 
                current = current.left 
            else: 
              
                pre.right = None
  
                # Increment count if the current 
                # node is to be visited 
                count += 1
                current = current.right 
  
    return count 

def findMedian(root):
    # code here
    # return the median
    if (root == None): 
        return 0
    count = counNodes(root) 
    currCount = 0
    current = root 
  
    while (current != None): 
      
        if (current.left == None): 
          
            # count current node 
            currCount += 1
  
            # check if current node is the median 
            # Odd case 
            if (count % 2 != 0 and 
                currCount == (count + 1)//2): 
                return prev.data 
  
            # Even case 
            elif (count % 2 == 0 and 
                    currCount == (count//2)+1): 
                return (prev.data + current.data)//2
  
            # Update prev for even no. of nodes 
            prev = current 
  
            #Move to the right 
            current = current.right 
          
        else: 
          
            """ Find the inorder predecessor of current """
            pre = current.left 
            while (pre.right != None and 
                    pre.right != current): 
                pre = pre.right 
  
            """ Make current as right child 
                of its inorder predecessor """
            if (pre.right == None): 
              
                pre.right = current 
                current = current.left 
            else: 
              
                pre.right = None
  
                prev = pre 
  
                # Count current node 
                currCount+= 1
  
                # Check if the current node is the median 
                if (count % 2 != 0 and 
                    currCount == (count + 1) // 2 ): 
                    return current.data 
  
                elif (count%2 == 0 and 
                    currCount == (count // 2) + 1): 
                    return (prev.data+current.data)//2
  
                # update prev node for the case of even 
                # no. of nodes 
                prev = current 
                current = current.right 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        s=input()
        root=buildTree(s)
        print(findMedian(root))

# } Driver Code Ends