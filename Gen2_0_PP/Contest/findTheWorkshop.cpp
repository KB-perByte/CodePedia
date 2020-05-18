
#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
#define int long long int
#define vi vector<int>
int32_t main()
{
 ios_base::sync_with_stdio(false);cin.tie(NULL); cout.tie(NULL);
  int n,m;
   cin>>n>>m;
    vi group(n);
    for(int i=0;i<n;i++) cin>>group[i];
    vi pref(n);
    pref[0]=group[0];
    for(int i=1;i<n;i++)
    {
        pref[i]= pref[i-1]+group[i];
    }
    while(m--)
    {
        int x;cin>>x;
        auto lb= lower_bound(pref.begin(),pref.end(),x);
        int len= lb-pref.begin();
        cout<<len+1<<" "<<*lb-x<<endl;
    }
    
}





# function to find cumulative sum of array 
from itertools import accumulate 
prfixsim = []
def cumulativeSum(input): 
	print ("Sum :", list(accumulate(input))) 
    
# Driver program 
if __name__ == "__main__": 
	input = [4, 6, 12] 
	cumulativeSum(input) 
    (list(accumulate(input)))