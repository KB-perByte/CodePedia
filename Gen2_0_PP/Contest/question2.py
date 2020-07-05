'''
XYZ Company has contacted Programming Pathshala to refer students for them.

PPa already gives a rating to each student on the basis of their performance in the workshop and the relating contests.

It is known that the last time a student with rating x was able to clear the XYZ Company's interview. This time, they want to try a student with rating just less than x and the student with rating just greater than x.

They want to know the difference in the ratings of the two students, one having rating just higher than x and the other one having rating just lower than x. Can you help them find this difference?

Note that there can be persons with rating exactly x in this batch too, but you don't need to consider them in calculating the greater or smaller elements.

Input Format

First line of input consists of two space separated integers, N the number of students that PPa have and Q the number of queries for x that they want to do.

Second line of input consists of N integers, which represents the ratings of the students.

The next Q lines each consists of a single integer x.

Constraints

2 <= N <= 100000

1 <= A[i] <= 10000000000

1 <= Q <= 100000

1 <= x <= 10000000000

Output Format

Output Q lines, the answer for each query, which is the difference of the just greater and just smaller element of number x.

Sample Input 0

7 7
2 2 5 6 8 8 12
1
2
3
6
8
12
15
Sample Output 0

-1
-1
3
3
6
-1
-1
'''