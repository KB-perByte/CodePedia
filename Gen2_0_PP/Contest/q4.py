''' Question 4 - contest 3
Debrup lives in Infiniteland.In Infiniteland time never moves in periodic fashion. Debrup is a very competitive person. Now, one day he goes to a horse race and wants to bid for the winning horse. There are N horses competing in the race. Now because Debrup wants to win the race, he bribes his friend Dheeraj and comes to know that the kth horse will win the race.

But there is a rule for bidding in the race. The person going at the ith position gets to bid only for the ith horse. Now Debrup comes to knows the timings of the remaining N-1 bidders that is when they will bid for the horses by bribing his another friend Vikhyat who is also in the organizing team of the horse race.

Given the timings of the N-1 bidders and an integer k , Debrup wants to know the interval of time when he should go to bid such that he wins the race and make his girlfriend happy.

The bidding begins at t=0 and ends at t=1000000.

It is always guaranteed that between any 2 bidders there is a time difference of atleast 2

Update: It is guaranteed that the answer will always exist.

Input Format

First line contains 2 integers N and k where N is the number of bidders and k is the index of the horse which wins the race.

Each of the following N-1 lines contains an integer ti which represents the time at which the ith person bids.

Constraints

1 <= N <= 1000

1 <= k <= N

0 <= yi <= 1000000

Output Format

Print 2 space separated integers in a line denoting the starting and ending time (both inclusive) between which Debrup should bid in order to win the race.

Sample Input 0

3 3
7
4
Sample Output 0

8 1000000
Sample Input 1

5 3
8
2
4
12
Sample Output 1

5 7
Explanation 1

Sample Case 1:

The second bidding takes place at t=7. So, to be the third bidder (as k=3), Debrup must bid between t=8 and t=1000000 (both inclusive).

Sample Case 2:

The second bidding takes place at t=4 and the next bidding takes place at t=8. So, to be the third bidder (as k=3), Debrup must bid between t=5 and t=7 (both inclusive).
'''