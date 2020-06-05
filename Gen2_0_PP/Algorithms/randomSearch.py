
import random

def my_function(x):
  return (1-x[0])**2 + 100*(x[1] - x[0]**2)**2


def optimize(gridAlt, ackLimit, fn):
  length = len(gridAlt)
  axis_f = 9999.0

  axis_x = [None]*length

  for i in range(ackLimit):
    temp_x = [gridAlt[d][0] + random.random()*(gridAlt[d][1] - gridAlt[d][0]) for d in range(length)]
    temp_f = fn(temp_x)
    if temp_f < axis_f: 
      axis_f = temp_f
      axis_x = temp_x


  return {'axis_x': axis_x, 'axis_f': axis_f}

gridAlt = [[-1,5], [-1,5]]
result = optimize(gridAlt, 10000, my_function)
print(result) 