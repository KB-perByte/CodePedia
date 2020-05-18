'''
There is a straight line with N points. A coin is located at each point starting from 1 and ending at N.

At N+1 th position, an additional M coins are kept.

A person starts walking with a bag from position 0 towards position N+1. At each position, i where 1 <= i <= N :

He collects the coin present at the position i.

If i divides both N and M, he empties his bag by throwing away all the coins he had collected till now.

Finally he collects the M coins present at position N+1.

Can you tell how many coins does the person has at the end of this process?

Input Format

The first line of input contains an integer T, which denotes the number of test cases.

Each line of test cases contains two integers N and M.

Constraints

1 <= T <= 10

1 <= N <= 10^10

1 <= M <= 10^6

Output Format

For each test case, in a separate line, output the number of coins that the person has after following the steps mentioned in the problem statement.

Sample Input 0

3
1 5
2 3
5 5
Sample Output 0

5
4
5
Explanation 0

Case 2: The person starts at position 1. He collects coin 1. 2%1 == 0 and 3%1 == 0. So, he throws away the collected coin.

Next, he goes to 2. 3%2 != 0. He has 1 coin.

Next, he collects the 3 remaining coins. So, total coins = 4.
'''
import math 

def sumOfDigitsFrom1ToN(n) : 
	if (n<10) : 
		return (n*(n+1)/2) 
	d = (int)(math.log10(n)) 
	a = [0] * (d + 1) 
	a[0] = 0
	a[1] = 45
	for i in range(2, d+1) : 
		a[i] = a[i-1] * 10 + 45 * (int)(math.ceil(math.pow(10,i-1))) 
	p = (int)(math.ceil(math.pow(10, d))) 
	msd = n//p 
	return (int)(msd * a[d] + (msd*(msd-1) // 2) * p +
		msd * (1 + n % p) + sumOfDigitsFrom1ToN(n % p)) 

def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

t = int(input())
while(t):
    t-=1
    arr = []
    # arr = list(map(int,input().split()))
    # a = compute_hcf(arr[0], arr[1])
    # _a = sumOfDigitsFrom1ToN(a)
    # _a1 = sumOfDigitsFrom1ToN(arr[0])

    # if int(_a1 - _a) == 0:
    #     print(int(arr[1]))
    # else:
    #print((int(_a1 - _a)-1)+int(arr[1]))

    arr = list(map(int,input().split()))
    a = compute_hcf(arr[0], arr[1])
    print(int((arr[0] - a) + arr[1]))



