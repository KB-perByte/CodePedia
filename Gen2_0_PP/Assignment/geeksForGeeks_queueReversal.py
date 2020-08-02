def reverseQueue(q):
    #add code here
    stack = []
    while not q.empty():
        stack.append(q.queue[0])
        q.get()
    while len(stack)!=0:
        q.put(stack[-1])
        stack.pop()
    return q
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n+1)
        for j in a:
            q.put(j)
        q=reverseQueue(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends