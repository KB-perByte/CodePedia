/* Question 2 - contest 3
Siddhant likes Permutations and Combinations.

Aware of his interests, his Math professor asks him a simple question.

He gives him a pile of currency notes. He is allowed to remove a finite number of notes from the top and bottom of the pile.

What is the number of ways in which he can remove the notes such that the final pile that is left has a total currency value = k, where k is a constant?

Input Format

The first line contains N the number of notes in the pile.

The second line contains k the constant value he is interested in (refer problem statement details as above).

The third line contains N space separated positive integers (A1 through An) : the values of the currency notes from top to bottom.

Constraints

1<=N<=100000

1<=k<=1000000000

1<=Ai<=100000

Output Format

A single positive integer: the number of ways he can remove some notes from the top and bottom such that the sum of the remaining notes in the pile = k.

Sample Input 0

5
3
1 2 3 4 5
Sample Output 0

2
*/

#include<bits/stdc++.h>
using namespace std;

int func(int *arr,int n,int k)
{
    int curr_sum=arr[0];
    int start=0;
    int ans=0;
    for(int i=1;i<n;i++)
    {
        while(curr_sum>k)
        {
            curr_sum-=arr[start];
            start++;
        }
        if(curr_sum==k)
        {
            ans++;
        }
        curr_sum+=arr[i];

    }
    while(curr_sum>k)
        {
            curr_sum-=arr[start];
            start++;
        }
    if(curr_sum==k)
    {
        ans++;
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    int n,k;
    cin>>n>>k;
    int *arr=new int[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    cout<<func(arr,n,k)<<endl;
    delete [] arr;
    return 0;
}