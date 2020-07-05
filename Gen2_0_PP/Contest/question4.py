'''
Programming Pathshala is organizing a workshop and want to have K students in this workshop.

N (N > K) students have filled willingness to join the workshop.

From the experiences of the previous workshop, the organizers are able to deduce a number a[i] for each student that represents the number of phone calls that need to be made to the ith student in order for him to register and pay the fee.

The person that needed to do this job of calling has lost these numbers a[i] and thus uses a strategy for getting the registerations.

He starts by calling every person once, then waits for any registrations. Next, he again calls the participants not registered yet for the second time and waits. He keeps continuing this till K people have registered.

You have to calculate the number of calls that he has to make.

Input Format

First line contains an integer T (the number of testcases).

Then first line of each test case contains an integer N (the number of students).

Then N space separated integers follow which are the number of calls to be made to each person.

Last line of each test case consists of an integer K, the number of registrations needed.

Constraints

1<=T<=10

1<=N,S[i]<=10^5

1<=K<=N

Output Format

For each case print in a new line print the number of calls the person needs to make

Sample Input 0

2
2
5 11
1
3
5 77 2
2
Sample Output 0

10
12
Explanation 0

In the first test case, he calls all the people 5 times before the first person registers, making total calls as 10.

In second case he first makes calls to everyone 2 times, before one of them registers. Then another 3 calls to remaining 2 candidates, making total calls to **3 * 2 + 2 * 3 = 12 **
'''