class CustomStack:
    def __init__(self):
        self.stack = []
        self.maxima = []
     
    def push(self, value):
        self.stack.append(value)
        if not self.maxima or value >= self.maxima[-1]:
            self.maxima.append(value)
         
    def printMax(self):
        print self.maxima[-1]
     
    def pop(self):
        value = self.stack.pop()
        if value == self.maxima[-1]:
            self.maxima.pop()
 
def main():
    cs = CustomStack()
     
    N = int(raw_input())
     
    for _ in xrange(N):
        unknown = raw_input()
         
        command = unknown[0]
         
        if command == '1':
            cmd, value = map(int, unknown.split())
            cs.push(value)
        elif command == '2':
            cs.pop()
        else:
            cs.printMax()
     
 
 
if __name__ == '__main__':
    main()
