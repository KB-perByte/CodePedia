''' Question 5 - contest 3
Everyone knows about James Bond and his famous 007. This task is simple. Bond has a length known as Bond Length (which is of length 7). You are given a character matrix where 'X' denotes Bond Code and '.' represents fake code.

James Bond Collects the consecutive codes (only of length 7).By consecutive we mean that we can collect them one after another.He is able to move in the four directions: North, South, West and East.

Input Format

Input starts with an integer T, representing the number of test cases (1<=T<=20). Each test case consists of a matrix, described as follows:

An integer N (1<=N<=8), representing the side length of the square-shaped matrix. N lines follow, N characters each. A 'X' character represents an James Code, and a '.' represents a Fake Code.

Constraints

1<=T<=20

1<=N<=8

Output Format

For each test case print the number of unique bond lengths on a single line.

Sample Input 0

1
3
XXX
X..
XXX
Sample Output 0

1
'''

R = 4
C = 4

def countPaths(maze): 
	if (maze[0][0] == -1): 
		return 0

	for i in range(R): 
		if (maze[i][0] == 0): 
			maze[i][0] = 1
		else: 
			break

	for i in range(1, C, 1): 
		if (maze[0][i] == 0): 
			maze[0][i] = 1
		else: 
			break

	for i in range(1, R, 1): 
		for j in range(1, C, 1): 
			if (maze[i][j] == -1): 
				continue
			if (maze[i - 1][j] > 0): 
				maze[i][j] = (maze[i][j] +
							maze[i - 1][j]) 
			if (maze[i][j - 1] > 0): 
				maze[i][j] = (maze[i][j] +
							maze[i][j - 1]) 
	if (maze[R - 1][C - 1] > 0): 
		return maze[R - 1][C - 1] 
	else: 
		return 0


if __name__ == '__main__': 
	maze = [[0, 0, 0, 0], 
			[0, -1, 0, 0], 
			[-1, 0, 0, 0], 
			[0, 0, 0, 0 ]] 
	print(countPaths(maze)) 

