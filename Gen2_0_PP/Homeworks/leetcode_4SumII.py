class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB_dict = {}
        for i in A:
            for j in B:
                AB_dict[i+j] = AB_dict.get(i+j,0)+1
                
        CD_dict = {}
        for i in C:
            for j in D:
                CD_dict[i+j] = CD_dict.get(i+j,0)+1
                
        #print(AB_dict,CD_dict)
        A = list(AB_dict)
        B = list(CD_dict)
        A.sort()
        B.sort()
        #print(A,B)
        
        def binary_search(arr,start,end,target):
            while start<=end:
                mid = (start+end+1)//2
                if arr[mid]+target==0:
                    return arr[mid]
                elif arr[mid]+target<0:
                    start = mid+1
                else:
                    end =mid-1
            return None
        
        res = 0
        for i in A:
            c = binary_search(B,0,len(B)-1,i)
            if c== None:
                continue
            else:
                res+=AB_dict.get(i)*CD_dict.get(c)
                
        
        return res