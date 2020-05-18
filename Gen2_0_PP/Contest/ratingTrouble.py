'''
There has been a recent codeforces contest that the students of the Genesis 1.0 have attempted.

After the contest, they are trying to predict their ratings. There has been a hack in the codeforces server that will lead to the rating of every person after the contest getting updated to the closest prime number to their rating before the contest.

In case, there are multiple ratings closest to the initial rating that are prime, the hacker has ensured that the rating will be updated to the lowest one.

Can you help the participants to determine their rating after the contest?

Input Format

The first line of input contains T, the number of students who wants to calculate their ratings.

The next T lines contain integer N, rating of the person.

Constraints

1 <= T <= 1000

1 <= N <= 1000000

Output Format

Output T lines, each line containing the result of the ith query.

Sample Input 0

3
10
20
30
Sample Output 0

11
19
29
Explanation 0

For the first test case, since the number 11 is closer to 10, than 7 (|11-10|<|10-7|), thus 11 is the correct answer.

Simlilarly for second test case.

For the third test case, since 2 closest primes are possible (viz. 29 and 31), we report the smaller one i.e 29.

Submissions: 38
Max Score: 100
Difficulty: Medium
Rate This Challenge:

    
More
 
'''
def getPrimes(limit):
    primes = []
    numbers = [True] * limit
    for i in range(2, limit):
        if numbers[i]:
            primes.append(i)
            for n in range(i ** 2, limit, i):
                numbers[n] = False
    return primes


t = int(input())
while(t):
    t-=1
    number = int(input())
    primes = getPrimes(number + 100)
    maxDist = 99999999
    numb = 0
    for p in primes:
        if abs(number - p) < maxDist:
            maxDist = abs(number - p)
            numb = p

    print(numb)
