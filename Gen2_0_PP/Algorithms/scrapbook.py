''' keep it empty '''
import time

def random_number(minimum,maximum):
    now = str(time.clock())
    rnd = float(now[::-1][:3:])/1000
    return minimum + rnd*(maximum-minimum)

print(random_number(0,1))