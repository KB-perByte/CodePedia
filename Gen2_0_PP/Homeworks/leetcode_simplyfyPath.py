class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        l = path.split('/')
        for i in range(len(l)):
            if(l[i]=='..' and len(stack)!=0):
                stack.pop()
            else:
                if(len(l[i])!=0 and l[i]!='.' and l[i]!='..'):
                    stack.append(l[i])
                else:
                    continue
        if(len(stack)==0):
            return "/"
        string = ""
        while(len(stack)!=0):
            string = '/' + stack.pop() + string 
        return string