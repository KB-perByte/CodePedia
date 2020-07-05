'''
Vivek is planning a study plan for the students of his workshop. He knows that a person can clear his target company's interview by spending a hours studying and b hours practicing problems iff a + b/2 >= x. He knows the value of the magic number x.

Vivek also knows that if a person studies for k hours, he/she is bound to get bored and will switch to practicing instead.

Vivek decides to check the students after every z hour and ask them to start studying back in case they are practicing.

Find out in how much time will the person be ready for the company's interview.

Input Format

The only line of input consists of 3 integers, k, z, x.

Constraints

1 <= k, z, x <= 10^10

Output Format

Output a single float number which denote the number of hours it will take for the person to be ready for the interview.

Sample Input 0

3 2 6
Sample Output 0

6.5
Explanation 0

In this example, the students will first start studying and study for 3 hours.

Next, they will start practising at 3rd hour. Vivek checks on them at 2nd hour, 4th hour and so on. At 3rd hour, Vivek asks them to switch back to studying.

Now, they will study till 6.5th hour as after that they have studied for 5.5 hours and practiced for 1 hour and 5.5/1 + 1/2 = 5.5 + 0.5 >= 6.

Thus, they are fully prepared after 6.5 hours.

Sample Input 1

4 2 20
Sample Output 1

20.0
'''