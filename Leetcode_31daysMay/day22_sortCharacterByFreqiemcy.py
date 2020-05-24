class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        
        res = []
        sList = list(s)
        N = len(sList)
        record = [[] for i in range(N)]
        dic = {}
        
        for ch in sList:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
                
        for k, v in dic.items():
            record[v-1].append(k)
            
        
        for i in range(N-1, -1, -1):
            if record[i] != []:
                for ch in record[i]:
                    res += [ch] * (i+1)
        return "".join(res)
        
        