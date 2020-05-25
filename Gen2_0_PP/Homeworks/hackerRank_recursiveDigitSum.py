#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    sumEach = (sum(int(i) for i in n) * k)
    if sumEach < 10:
            return sumEach
    else:
            return superDigit(str(sumEach), 1)

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

'''integer based approach '''
def digSum(n): 
	if n == 0: 
		return 0
	return (n % 9 == 0) and 9 or (n % 9) 

def repeatedNumberSum(n, x): 
	sum = x * digSum(n) 
	return digSum(sum) 

n = 24; x = 3
print(repeatedNumberSum(n, x)) 
''' end '''
