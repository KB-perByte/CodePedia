import sys
import math
#from queue import *
#import random
#sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
 
############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input()))
def inara():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
################################################################
############ ---- THE ACTUAL CODE STARTS BELOW ---- ############

t=inp()

for _ in range(t):
    n=inp()
    arr=inara()
    if max(arr) == n:
        print('YES')
        print(1, n-2 ,n-1)
    else:
        print('NO')
