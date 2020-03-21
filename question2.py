#!/usr/bin/python

'''
2. Simulate Stopwatch Program
a. Desc -> Write a Stopwatch Program for measuring the time that elapses between the 
start and end clicks
b. I/P -> Start the Stopwatch and End the Stopwatch
c. Logic -> Measure the elapsed time between start and end
d. O/P -> Print the elapsed time
'''
import time

print ''' Input as needed: \n Type 1 to Start the Stopwatch \n Type 2 to End the Stopwatch  '''

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

flag = True
while flag:
    choice = input("Input : ")
    if choice == 1 or choice == '1':
        start = time.time()
        print ("Type 2 to Stop Stopwatch \nType 3 to Exit")
        choice = input("Input in : ")
        end = time.time()
        if choice == 2 or choice == '2':
            time_elapsed = end - start
            time_convert(time_elapsed)
        else:
            print "Closing.."
            exit()
    else:
        print "Closing.."
        exit()
