
def minimumSwaps(arr): 
	count = 0; 
	i = 0; 
	while (i < len(arr)): 
		if (arr[i] != i + 1): 

			while (arr[i] != i + 1): 
				temp = 0; 
				temp = arr[arr[i] - 1]; 
				arr[arr[i] - 1] = arr[i]; 
				arr[i] = temp; 
				count += 1; 
		i += 1; 
	
	return count; 

 
if __name__ == '__main__': 
    n = int(input())
    while(n):
        n-=1
        x = int(input())
        arr = list(map(int,input().split()))
        print(minimumSwaps(arr))
	

#try 2
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
	ara=inara()
	l=0
	while l<n and ara[l]==l+1:
		l+=1
	r=n-1
	while r>=0 and ara[r]==r+1:
		r-=1
	
	if l>r:
		print(0)
	else:
		alada=0
		for i in range(l,r+1):
			if ara[i]==i+1:
				alada+=1
		
		if alada:
			print(2)
		else:
			print(1)
			
#try 3
t = int(input())
for _ in range(t):
	n = int(input())
	a = [int(num) for num in input().split()]
	cnt = 0
	if(a[0]==1):
		prev = True
	else:
		cnt=1
		prev = False
	for i in range(1,n):
		if(a[i]==i+1):
			prev = True
		else:
			if prev:
				cnt+=1
			prev = False
	print(min(cnt,2))