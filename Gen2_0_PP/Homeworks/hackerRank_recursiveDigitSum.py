#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
ans = 0 
ans2 = 0

def superDigit(n, k):
    global ans

    def sumMe(n):
        global ans2
        ans2 += (n % 10)
        if n == 0:
            return
        sumMe(n//10)

    def computeN(n, k):
        global ans
        global ans2
        k-=1
        if k == 0: 
            return 
        sumMe(n)
        ans+=ans2
        computeN(n, k)
    
    computeN(n, k)

    def finalcomp(ans):
        if ans//10 == 0:
            return ans
        sumMe(ans)
        finalcomp(ans)
    
    finalcomp(ans)
    return ans

'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
'''

print(superDigit(148, 3))