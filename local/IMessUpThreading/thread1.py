import threading 

class PrimeNumber(threading.Thread):
    prime_numbers = {} 
    lock = threading.Lock()
    
    def __init__(self, number): 
        threading.Thread.__init__(self) 
        self.Number = number
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[number] = "None" 
        PrimeNumber.lock.release() 
 
    def run(self): 
        counter = 2
        res = True
        while counter*counter < self.Number and res: 
            if self.Number % counter == 0: 
               res = False 
            counter += 1 
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[self.Number] = res 
        PrimeNumber.lock.release() 

threads = [] 
while True: 
    inp = input("number: ")
    inp = int(inp)
    if inp < 1: 
        break 
 
    thread = PrimeNumber(inp) 
    threads += [thread] 
    thread.start() 
 
for x in threads: 
    x.join()