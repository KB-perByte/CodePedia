from threading import Thread
import time

def sub_worker(id):
    print("SubWorker started from thread", id)
    while True:
        print("Subworking...")
        time.sleep(5)
        
def worker(id):
    print("Worker started from thread", id)
    count = 1
    while count < 5:
        print("Working...")
        tmp_thread = Thread(target=sub_worker, args=[count])
        tmp_thread.start()
        count +=1
        time.sleep(1)
    raise EnvironmentError("Tired of working")

main = Thread(target=worker, args=[0])

main.start()