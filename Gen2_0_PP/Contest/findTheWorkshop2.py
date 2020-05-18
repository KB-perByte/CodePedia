'''
Programming Pathshala has launched N workshops. Each of the courses have a seat limit represented by an array of integers a[i]

To segregate students into batches for these workshops, they have conducted a contest. The students with ranks 1 to a[0] will be a part of the first workshop, those with ranks between a[0] + 1 and a[0] + a[1] will be a part of the second workshop and so on.

Given rank of M different students, for each of them, find the workshop number and his/her rank in that workshop batch.

For example, if the limits of workshops are represented by [30, 20, 30, 10], if a person has rank 40, he will be a part of the second workshop and will have 10th rank in the workshop.

Note that the rank will always be within the maximum number of seats in the workshop.

Input Format

The first line of input consists of two integers N and M, the number of workshops and the number of queries.

The next line of input consists of N space separated integers, denoting the number of seats in each of the workshop, array a[i].

The next line of input consists of M space separated integers, denoting the ranks of the student for which we have queried, represented by array b[i].

Constraints

1 <= N, M <= 200000

1 <= a[i] <= 10^10

1 <= b[i] <= sum(a[i])

Output Format

For each of the M queries, output 2 space separated integers in a new line denoting the workshop number and the person's rank in the workshop.

Sample Input 0

4 2
30 20 30 10
85 40
Sample Output 0

4 5
2 10
Explanation 0

In this case, students with rank (1, 30) will be in first group.

Those with ranks in (31, 50) will be in second group.

Those with ranks in (51, 80) will be in third group.

Those with ranks in (81, 90) will be in fourth group
'''
from itertools import accumulate
from bisect import bisect_right, bisect_left

input1 = list(map(int,input().split()))
input2 = list(map(int,input().split()))

prefixSm = []
prefixSm = (list(accumulate(input2)))

input3 = list(map(int,input().split()))

def findLowerbound(a, x):
    i = bisect_left(a, x)
    if i != len(a):
        if i == 0:
            return i+1 , x
        else:
            return i+1 , x - a[i-1]

#print("prefix sum", prefixSm)
for i in range(len(input3)):
    workshopNo , rank = findLowerbound(prefixSm, input3[i])
    print(workshopNo, rank)
    


