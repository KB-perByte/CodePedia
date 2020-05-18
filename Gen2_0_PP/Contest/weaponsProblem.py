'''
Daenerys has N types of weapons. There are Ai number of weapons of type i (1 <= i <= N). She wants to distribute these weapons among K soldiers. She wants to distribute them in such a way that:

All soldier get equal number of weapons.
All the weapons which a soldier gets must be of same type.
As she wants to make all of them more powerful so she wants to give as many weapons as possible. Help Daenerys in finding out what is the maximum number of weapons which a soldier can get.

Input Format

The first line consists two space seperated integer N and K.

The second line consists of N space seperated integers A1, A2, A3.... An, as described above.

Constraints

1 <= N <= 100000

1 <= Ai, K <= 1,000,000,000

Output Format

Output a single integer denoting the maximum weapons a soldier can get .

Sample Input 0

3 2 
3 1 4
Sample Output 0

3
Explanation 0

She can give 3 weapons of type 1 to first soldier and 3 weapons of type 3 to second soldier.

'''

def binarySearch(array, l, r, toSearch):  #not so needed
    while l <= r: 
        mid = l + (r - l)//2
        if array[mid] == toSearch: 
            return mid 
        elif array[mid] < toSearch: 
            l = mid + 1
        else: 
            r = mid - 1
    return -1

def checkDistribution(lst, mid , k):
    s = 0
    for i in range(len(lst)):
        s+=lst[i]//mid
    print('val of s',s)
    print('val of k',k)
    return s>=k

def makimumWeapons(lst,k):
    l = min(lst)
    h = max(lst)
    while h >= l:
        mid = l+(h-l)//2
        print("value of l and h", l ,h)
        if checkDistribution(lst, mid, k):
            if not checkDistribution(lst, mid+1, k):
                return mid
            else:
                l = mid + 1 
        else:
            h = mid - 1
    return 0

import sys 

def get_ints(): return list(map(int, sys.stdin.readline().strip().split())) 

input1 = list(map(int,input().split()))
#input2 = list(map(int,input().split()))
input2 = get_ints() 
print(makimumWeapons(input2, input1[1]))
