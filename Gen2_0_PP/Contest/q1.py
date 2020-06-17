''' Question 1 - contest 3
Anoop is planning a new workshop called "Genesis" for the students of Programming Pathshala. This workshop will focus on all the topics from basic to advanced that are required to get into any major company.

He has to come up with a fee for the contest. He like the numbers 5 and 9 a lot and wants to have the fee with only these numbers. Also, he wants the fee number to have equal number of 5 and 9. For example, 5599, 9595, 95 are valid fee but 99, 759, 595, etc are invalid.

Anoop knows a value x which is the minimum value of the fee that should be there for the course. You need to find the smallest valid fee just greater than x.

Input Format

The only line of input consists of an integer x, which tells the minimum fee that should be there.

Constraints

1 <= x <= 10^9

Output Format

Output a single integer, the minimum fee that Anoop can keep if the fee has to be a lucky number

Sample Input 0

9800
Sample Output 0

9955
Explanation 0

If we write all the possible fee values in increasing order, we get 59, 95, 5599, 5959, 5995, 9559, 9595, 9955, ...

The number just greater than 9800 is 9955

Sample Input 1

59
Sample Output 1

59
Explanation 1

59 is itself a valid fee value as it has equal number of 5 and 9 in it.
'''

import math 

def countDigit(n): 
	return math.floor(math.log(n, 10))

def findRec(res, a, x, b, y, n): 
	f = open("Gen2_0_PP/Contest/output.txt", "+a")
	ss = 'res->' + str(res) + ' a->' + str(a) + ' x->' + str(x) + ' b->' +  str(b) + ' y->' + str(y) + ' n->' + str(n)+'\n'
	f.write(ss)
	f.close()
	#print(res, a, x, b, y, n)
	if (res > 1e11): 
		return 1e11
	if (x == y and res >= n): 
		return res 
	return min(findRec(res * 10 + a, a, x + 1, b, y, n), findRec(res * 10 + b, a, x, b, y + 1, n)) 

def numFunc(n, a, b): 
	ans, x, y= 0 ,0 ,0
	return findRec(ans, a, x, b, y, n) 

N = int(input())
print(numFunc(N, 5, 9)) 

