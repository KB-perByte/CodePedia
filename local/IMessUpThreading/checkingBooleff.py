''' is bool slower than not not? not not failed when it had to make it as a object'''
import timeit
import time
from threading import Thread

prob_slow = """
class SlowClass:
    def __init__(self):
        self.data = 5
    def __bool__(self):
        return bool(self.data)
sC = SlowClass()
"""

prob_fast = """
class FastClass:
    def __init__(self):
        self.data = 5
    def __bool__(self):
        return not not self.data
fC = FastClass()
"""

itr, total = 5, 5
a1 , a2, b1, b2 = 0, 0, 0, 0

def loopme(a1, a2, b1, b2):
    a1 += timeit.timeit('sC.__bool__()', prob_slow)
    a2 += timeit.timeit('fC.__bool__()', prob_fast)
    b1 += timeit.timeit('if sC:pass', prob_slow)
    b2 += timeit.timeit('if fC:pass', prob_fast)

for i in range(total):
    t = Thread(target=loopme, args=(a1, a2, b1, b2))
    t.start()

for i in range(total):
    # t = Thread(target=loopme, args=(a1, a2, b1, b2))
    t.join()

print(a1/total)
print(a2/total)
print(b1/total)
print(b2/total)