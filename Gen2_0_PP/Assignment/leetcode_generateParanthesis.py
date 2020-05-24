class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst=['']*(2*n)
        res=[]
        def helper(lst,idx,n,beg,end):
            if end==n:
                res.append(''.join(lst))
            else:
                if beg<n:
                    lst[idx]="("
                    helper(lst,idx+1,n,beg+1,end)
                if end<beg:
                    lst[idx]=")"
                    helper(lst,idx+1,n,beg,end+1)
        helper(lst,0,n,0,0)
        return res