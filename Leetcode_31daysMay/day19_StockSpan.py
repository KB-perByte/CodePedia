class StockSpanner(object):

    def __init__(self):
        self.st=[]
        self.d=0        


    def next(self, price):
        """
        :type price: int
        :rtype: int
        """

        l=-1
        while self.st and self.st[-1][0]<=price:
            self.st.pop()

        if self.st:
            l=self.st[-1][-1]

        ans=self.d-l
        self.st.append((price,self.d))

        self.d+=1

        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)