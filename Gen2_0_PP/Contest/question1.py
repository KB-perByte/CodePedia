'''
Vivek wants to climb N stairs in front of him. He is very athletic guy and can jump 3 stairs ahead easily. So, from any stair x, he can directly jump to stair x+1, x+2 or x+3.

Some stairs are slippery and climbing on them is dangerous. So, Vivek would not like to never be on that stair during his climb.

He wants to know the number of ways to reach the stair N. Can you help him calculate this?

Input Format

First line of input consists of a single number N, the number of stairs that Vivek needs to climb.

Second line of input consists of a single number M, the number of stairs that are slippery.

The third line of input consists of M integers which denote the index of the stairs that are slippery.

Constraints

1 <= N <= 20

1 <= M, index of slippery stairs <= N

Output Format

Output a single integer, the number of ways to reach the Nth stair.

Sample Input 0

3
1
2
Sample Output 0

2
Explanation 0

Firstly, the person is at 0th step. In one jump, he can go to 1st, 2nd or 3rd step. Out of this, 2nd step is slippery and he won't step on that stair.

So, in first step, he will either jump to 1 or 3. When he jumps to 1st step, he can jump to 3rd step in next jump.

So, there are 2 possible ways.

0 -> 3

0 -> 1 -> 3
'''
'''
def countWays(n) : 
    res = [0] * (n + 1) 
    res[0] = 1
    res[1] = 1
    res[2] = 2
      
    for i in range(3, n + 1) : 
        res[i] = res[i - 1] + res[i - 2] + res[i - 3] 
      
    return res[n] 
  
# Driver code 
n = int(input())
x = int(input())
p = list(map(int, input().split()))
print(countWays(n)) 



'''
n = 3
X = [1,2,3]

def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in X:
        return 1 + sum(staircase(n - x, X) for x in X if x < n)
    else:
        return sum(staircase(n - x, X) for x in X if x < n)

print(staircase(n,X))