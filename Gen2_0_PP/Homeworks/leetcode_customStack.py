class CustomStack:

    def __init__(self, maxSize: int):
        self.item =  []
        self.size =  0
        self.maxsize = maxSize
        
    def push(self, x: int) -> None:
        if self.size < self.maxsize:
            self.item.append(x)
            self.size+=1

    def pop(self) -> int:
        if  self.size >0:
            self.size-=1
            return self.item.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < self.size:
                self.item[i] += val
            else:
                break


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)