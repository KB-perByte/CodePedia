#include <bits/stdc++.h>
#define ll long long int
using namespace std;
bool func(ll pages, ll *arr,ll m, ll n)
{ ll sum=0;
ll count=1;
    for(ll i=0;i<n;i++)
    {
        if(sum+arr[i]>pages)
        {
            count++;
            sum=arr[i];
            if(count>m)
            return false;
            
        }
        else
        {
            sum=sum+arr[i];
        }
    }
    return true;
}
int main() {
	ll t;
	cin>>t;
	while(t--)
	{
	    ll n; cin>>n;
	    ll *arr= new ll[n];
	    ll maxI= LLONG_MIN;
	    ll sum=0;
	    for(ll i=0;i<n;i++)
	    {
	        cin>>arr[i];
	        maxI= max(maxI, arr[i]);
	        sum+= arr[i];
	    }
	    ll m;
	    cin>>m;
	    if(m>n)
	    {
	        ll ans=-1;
	        cout<<ans<<endl;
	    }
	    else
	    {
	    ll l=maxI;
	    ll h= sum;
	    ll ans=-1;
	    while(l<=h)
	    {
	        ll mid= (l+h)/2;
	        if(func(mid, arr,m,n))
	        {
	            ans=mid;
	             if(func(mid-1, arr,m,n))
	                h=mid-1;
	             else
	             break;
	        }
	        else
	            l=mid+1;
	    }
	    cout<<ans<<endl;
	    }
	}
	return 0;
}