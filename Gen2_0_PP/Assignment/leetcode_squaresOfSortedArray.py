class Solution(object):
    
    def sortedSquares(self, a):
        # get first non neg index
        first = 0
        for i in range(len(a)):
            if a[i] >= 0:
                first = i
                break
        
		# square of each element
        for i in range(len(a)):
            a[i] = a[i] * a[i]
		
		# simply merge two sorted arrays
        return self.mergeTwoSortedArrays(a[:first][::-1], a[first:])
        
    def mergeTwoSortedArrays(self, a, b):
        
        i = j = 0
        res = []
        while i < len(a) and j < len(b) :
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
            
        while i < len(a):
            res.append(a[i])
            i += 1

        while j < len(b):
            res.append(b[j])
            j += 1
            
        return res