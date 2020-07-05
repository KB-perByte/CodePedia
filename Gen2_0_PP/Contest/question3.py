'''
There are N students in the current course of Programming Pathshala. As programming pathshala is a big supporter of group studies, it wants to form pairs of students to make them study together and learn from each other.

They have calculated the range of difficulty of problems that every student likes to solve, which is represented by range [l_i, r_i].

A pair of students will not enjoy the group sessions, if their difficulty ranges are disjoint. For example, if one student like problems of level [1,3] and other of level [6,10], they won't enjoy working together.

You have to find the number of such pair of students who will enjoy the session together.

Note: Two students who enjoy problems of difficulties [1,2] and [2,3] respectively will enjoy studying together.

Input Format

The first line of input contains N, the number of students

Next N lines each contain two integers, l and r that represent the range of difficulty of problem that each person will like.

Constraints

2 <= N <= 100000

1 <= l,r <= 1000000000

Output Format

Output a single integer, the number of possible pair of students that enjoy the session together.

Sample Input 0

4
8 10
4 9
6 7
1 2
Sample Output 0

2
Explanation 0

The pair [4,9] and [8,10] is one such pair which will enjoy sessions together.

Similarly, pair [4,9] and [6,7] is second such pair
'''