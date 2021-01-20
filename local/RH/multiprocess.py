import time
import multiprocessing


t1 = time.perf_counter()

def do_something():
    print("Start ")
    time.sleep(1)
    print("End ")

p1 = multiprocessing.Process(target=do_something, daemon= True)

p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

t2 = time.perf_counter()

print("{}".format(t2 - t1))